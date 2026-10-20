SELECT
  SUM(views) AS views,
  SUM(chats) AS chats,
  SUM(seller_responses) AS seller_responses,
  SUM(leads) AS leads,
  ROUND(100.0*SUM(chats)/NULLIF(SUM(views),0),2) AS view_to_chat_pct,
  ROUND(100.0*SUM(seller_responses)/NULLIF(SUM(chats),0),2) AS chat_response_pct,
  ROUND(100.0*SUM(leads)/NULLIF(SUM(seller_responses),0),2) AS response_to_lead_pct,
  ROUND(100.0*SUM(leads)/NULLIF(SUM(views),0),2) AS view_to_lead_pct
FROM listings;;
