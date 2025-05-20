# Write your MySQL query statement below
SELECT e.employee_id, e.name,
COUNT(e1.employee_id) AS reports_count,
ROUND(AVG(e1.age)) AS average_age
FROM Employees as e
JOIN Employees as e1 ON e.employee_id = e1.reports_to
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id;
