/* Write your T-SQL query statement below */
SELECT a.project_id, ISNULL(ROUND(SUM(b.experience_years) * 1.0/NULLIF(COUNT(b.experience_years),0),2),0) AS average_years
FROM Project a
LEFT JOIN employee b
ON a.employee_id = b.employee_id
GROUP BY project_id
ORDER BY a.project_id;