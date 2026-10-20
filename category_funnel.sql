SELECT category,
  SUM(views) AS views, SUM(chats) AS chats, SUM(leads) AS leads,
  ROUND(100.0*SUM(chats)/NULLIF(SUM(views),0),2) AS view_to_chat_pct,
  ROUND(100.0*SUM(leads)/NULLIF(SUM(views),0),2) AS view_to_lead_pct
FROM listings GROUP BY category ORDER BY view_to_lead_pct DESC;;
