/* Write your T-SQL query statement below */
-- SELECT a.user_id, ROUND(COALESCE(SUM(CASE WHEN b.action = 'confirmed' THEN 1 ELSE 0 END)/NULLIF(COUNT(b.user_id),0),0),2) AS confirmation_rate 
-- FROM Signups as a
-- LEFT JOIN Confirmations as b
-- ON a.user_id = b.user_id
-- GROUP BY a.user_id;
    
SELECT 
    a.user_id, 
    ROUND(
        COALESCE(
            SUM(CASE WHEN b.action = 'confirmed' THEN 1 ELSE 0 END) * 1.0
            / NULLIF(COUNT(b.time_stamp), 0), 
        0), 2) AS confirmation_rate 
FROM Signups AS a
LEFT JOIN Confirmations AS b
ON a.user_id = b.user_id
GROUP BY a.user_id;
