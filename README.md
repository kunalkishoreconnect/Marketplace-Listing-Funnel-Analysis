# Marketplace Listing Funnel Analysis

An OLX-style marketplace analytics case study that diagnoses how listings convert from **views → chats → seller responses → leads**, and identifies the highest-impact supply-side levers.

## Business question
Why do some listings generate buyer chats and leads while others receive views but fail to convert?

## Dataset
Synthetic marketplace dataset designed to resemble a classifieds platform:

- 6,000 listings across 6 categories and 6 Indian cities  
- 1,200 sellers, Individual and Dealer  
- 118,614 listing-level view/chat events  
- SQLite database: `marketplace.db`  
- Tables: `listings`, `sellers`, `listing_events`

## Funnel results
| Stage | Value | Conversion |
|---|---:|---:|
| Views | 104,621 | — |
| Chats | 13,993 | 13.37% of views |
| Seller responses | 8,568 | 61.23% of chats |
| Leads | 4,685 | 54.68% of responses |
| Overall view-to-lead | 4,685 | 4.48% of views |

## Key findings
1. **Listing quality is the strongest conversion lever.** High-quality listings convert at 13.67% view-to-chat versus 9.93% for medium-quality listings.
2. **Photos materially improve conversion.** Listings with 5+ photos convert at 14.15% view-to-chat, compared with 11.37% for listings with no photos.
3. **Seller responsiveness drives lead creation.** Dealers respond to 84.1% of chats versus 55.3% for individual sellers; dealer listings generate 5.99% view-to-lead conversion versus 4.08% for individual sellers.
4. **Listing engagement decays sharply after week 3.** Cohort retention falls from 90.7% in week 3 to 42.5% in week 4, suggesting a refresh/promotion opportunity for aging listings.
5. **Furniture has the best category-level conversion**, while Electronics has the weakest view-to-lead conversion.

## Recommended product actions
- Add a listing-quality prompt requiring at least 3 photos, price, and a minimum description length.
- Nudge individual sellers to respond within 6 hours; test a “Responsive Seller” badge.
- Refresh or discount-promote listings that receive no chats within 7 days.
- Prioritize Electronics listing-quality interventions because demand exists but conversion is weakest.

## Repository structure
```text
marketplace_funnel/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── listings.csv
│   ├── sellers.csv
│   └── listing_events.csv
├── results/
│   ├── funnel_overview.csv
│   ├── category_funnel.csv
│   ├── city_funnel.csv
│   ├── quality_bins.csv
│   ├── cohort_retention.csv
│   ├── seller_lever_ranking.csv
│   └── photo_impact.csv
├── sql/
│   ├── funnel_overview.sql
│   ├── category_funnel.sql
│   ├── city_funnel.sql
│   ├── quality_bins.sql
│   ├── cohort_retention.sql
│   ├── seller_lever_ranking.sql
│   └── photo_impact.sql
├── marketplace.db
└── README.md
```

## How to run
```bash
pip install streamlit pandas plotly
streamlit run app/streamlit_app.py
```

Place `streamlit_app.py` in the same folder as `marketplace.db`, or update the `DB` path in the app.

## Skills demonstrated
- SQL: window-style cohort logic, CTEs, conditional aggregation, funnel metrics  
- Analytics: conversion funnels, cohort retention, segmentation, opportunity sizing  
- Product thinking: marketplace health, seller trust, listing quality, experimentation candidates  
- Dashboarding: Streamlit and Plotly  
