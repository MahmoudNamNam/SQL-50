SELECT
  ROUND(
    COUNT(DISTINCT player_id) / 
    (
      SELECT COUNT(DISTINCT player_id) 
      FROM Activity
    ),2) AS fraction
FROM
  Activity
WHERE
  --* Check if the current player and event date (shifted by one day) match 
  (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
  IN (
    --* Subquery: Find the first login date for each player.
    SELECT 
      player_id, 
      MIN(event_date) AS first_login 
    FROM Activity
    GROUP BY player_id
  )
