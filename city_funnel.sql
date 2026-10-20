SELECT city,
  COUNT(*) AS listings, SUM(views) AS views, SUM(chats) AS chats, SUM(leads) AS leads,
  ROUND(100.0*SUM(chats)/NULLIF(SUM(views),0),2) AS view_to_chat_pct
FROM listings GROUP BY city ORDER BY views DESC;;
