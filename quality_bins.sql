SELECT CASE WHEN quality_score<.3 THEN '0 Low'
            WHEN quality_score<.5 THEN '1 Medium-Low'
            WHEN quality_score<.7 THEN '2 Medium'
            ELSE '3 High' END AS quality_band,
  COUNT(*) listings, SUM(views) views, SUM(chats) chats, SUM(leads) leads,
  ROUND(100.0*SUM(chats)/NULLIF(SUM(views),0),2) view_to_chat_pct,
  ROUND(100.0*SUM(leads)/NULLIF(SUM(views),0),3) view_to_lead_pct
FROM listings GROUP BY 1 ORDER BY 1;;
