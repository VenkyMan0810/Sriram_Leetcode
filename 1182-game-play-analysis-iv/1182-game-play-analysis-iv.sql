# Write your MySQL query statement below
With Firstlogin AS (
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id
)
SELECT
ROUND(1.0 * COUNT(DISTINCT a.player_id)/ (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM FirstLogin f
JOIN Activity a
ON f.player_id = a.player_id
AND a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);