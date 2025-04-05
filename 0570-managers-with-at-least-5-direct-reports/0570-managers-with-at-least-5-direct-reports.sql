/* Write your T-SQL query statement below */
-- SELECT b.name
-- FROM Employee AS a
-- RIGHT JOIN Employee AS b
-- ON a.managerId = b.id
-- GROUP BY a.managerId, b.name
-- HAVING COUNT(a.managerId) >= 5;


SELECT name
FROM Employee
WHERE id IN (
SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >= 5
);