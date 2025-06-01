# Write your MySQL query statement below
SELECT friends AS id,
    COUNT(*) AS num
FROM(
    SELECT requester_id as friends FROM RequestAccepted 
    UNION ALL
    SELECT accepter_id as friends FROM RequestAccepted
) as s
GROUP BY friends
ORDER BY num DESC
LIMIT 1;