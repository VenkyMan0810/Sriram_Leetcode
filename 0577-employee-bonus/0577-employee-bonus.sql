/* Write your T-SQL query statement below */
WITH cte1 AS (
SELECT a.name, b.bonus
FROM Employee A
LEFT JOIN Bonus b
ON a.empId = b.empId
)
SELECT name, bonus
FROM cte1
WHERE bonus < 1000 OR bonus IS NULL;