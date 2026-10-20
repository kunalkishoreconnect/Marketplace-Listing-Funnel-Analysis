import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Marketplace Listing Funnel Analysis", layout="wide")
st.title("Marketplace Listing Funnel Analysis")
st.caption("OLX-style marketplace: listing views → chats → seller responses → leads")

DB = "marketplace.db"
con = sqlite3.connect(DB)

@st.cache_data
def load(query):
    return pd.read_sql_query(query, con)

listings = load("SELECT * FROM listings")
funnel = load("SELECT * FROM funnel_overview")
category = load("SELECT * FROM category_funnel")
city = load("SELECT * FROM city_funnel")
quality = load("SELECT * FROM quality_bins")
cohort = load("SELECT * FROM cohort_retention")
seller = load("SELECT * FROM seller_lever_ranking")
photos = load("SELECT * FROM photo_impact")

st.sidebar.header("Filters")
cities = st.sidebar.multiselect("City", options=sorted(listings.city.unique()), default=sorted(listings.city.unique()))
cats = st.sidebar.multiselect("Category", options=sorted(listings.category.unique()), default=sorted(listings.category.unique()))
statuses = st.sidebar.multiselect("Listing status", options=sorted(listings.status.unique()), default=sorted(listings.status.unique()))

f = listings[listings.city.isin(cities) & listings.category.isin(cats) & listings.status.isin(statuses)]
total_views, total_chats, total_leads = f.views.sum(), f.chats.sum(), f.leads.sum()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Listings", f"{len(f):,}")
c2.metric("Views", f"{total_views:,}")
c3.metric("Chats", f"{total_chats:,}")
c4.metric("Leads", f"{total_leads:,}")

c5,c6,c7 = st.columns(3)
c5.metric("View → Chat", f"{100*total_chats/max(total_views,1):.2f}%")
c6.metric("Chat → Lead", f"{100*total_leads/max(total_chats,1):.2f}%")
c7.metric("View → Lead", f"{100*total_leads/max(total_views,1):.2f}%")

st.subheader("Conversion funnel")
funnel_df = pd.DataFrame({"Stage":["Views","Chats","Seller responses","Leads"],
 "Value":[f.views.sum(), f.chats.sum(), f.seller_responses.sum(), f.leads.sum()]})
fig = px.funnel(funnel_df, x="Value", y="Stage", title="Listing-to-lead funnel")
st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
left.subheader("Conversion by category")
left.plotly_chart(px.bar(category, x="category", y="view_to_chat_pct", color="category",
 title="View-to-chat conversion (%)"), use_container_width=True)
right.subheader("Supply and demand by city")
right.plotly_chart(px.bar(city, x="city", y=["listings","views"], barmode="group",
 title="Listings vs views by city"), use_container_width=True)

st.subheader("Listing-quality impact")
st.plotly_chart(px.bar(quality, x="quality_band", y="view_to_lead_pct",
 title="View-to-lead conversion by listing-quality band (%)"), use_container_width=True)

st.subheader("Listing cohort retention")
st.plotly_chart(px.line(cohort, x="week_offset", y="retention_pct", markers=True,
 title="Share of listings receiving views or chats after first activity (%)"), use_container_width=True)

st.subheader("Seller response and trust levers")
st.dataframe(seller, use_container_width=True)
st.plotly_chart(px.bar(photos, x="photo_band", y="view_to_chat_pct",
 title="View-to-chat conversion by photo count (%)"), use_container_width=True)

st.subheader("Opportunity finder")
opp = f.groupby(["category","city"]).agg(
    listings=("listing_id","count"), views=("views","sum"), chats=("chats","sum"),
    leads=("leads","sum")).reset_index()
opp["view_to_chat_pct"] = (100*opp.chats/opp.views.replace(0,pd.NA)).round(2)
opp["lead_per_1k_views"] = (1000*opp.leads/opp.views.replace(0,pd.NA)).round(1)
st.dataframe(opp.sort_values("lead_per_1k_views"), use_container_width=True)

st.download_button("Download opportunity table (CSV)", opp.to_csv(index=False).encode(),
 file_name="marketplace_opportunity_finder.csv")
