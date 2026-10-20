WITH first_event AS (
  SELECT listing_id, MIN(event_date) AS first_event_date
  FROM listing_events GROUP BY listing_id
),
cohort AS (
  SELECT e.listing_id,
         CAST((julianday(e.event_date)-julianday(f.first_event_date))/7 AS INTEGER) AS week_offset
  FROM listing_events e JOIN first_event f USING(listing_id)
  GROUP BY 1,2
)
SELECT week_offset,
  COUNT(DISTINCT listing_id) AS active_listings,
  ROUND(100.0*COUNT(DISTINCT listing_id)/
    (SELECT COUNT(DISTINCT listing_id) FROM cohort WHERE week_offset=0),1) AS retention_pct
FROM cohort GROUP BY week_offset ORDER BY week_offset;;
