SELECT s.seller_type,
  ROUND(AVG(l.response_time_hours),1) AS avg_response_hours,
  ROUND(100.0*SUM(l.seller_responses)/NULLIF(SUM(l.chats),0),1) AS response_rate_pct,
  ROUND(100.0*SUM(l.chats)/NULLIF(SUM(l.views),0),2) AS view_to_chat_pct,
  ROUND(100.0*SUM(l.leads)/NULLIF(SUM(l.views),0),2) AS view_to_lead_pct
FROM listings l JOIN sellers s USING(seller_id)
GROUP BY s.seller_type;;
