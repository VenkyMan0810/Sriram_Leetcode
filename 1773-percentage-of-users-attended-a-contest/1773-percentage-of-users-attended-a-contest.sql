/* Write your T-SQL query statement below */
SELECT b.contest_id,
ROUND((COUNT(b.user_id)*100.0/(SELECT COUNT(user_id) FROM Users)),2) AS percentage
FROM USERS as a
JOIN Register as b
ON a.user_id = b.user_id
GROUP BY b.contest_id
ORDER BY percentage DESC, contest_id;