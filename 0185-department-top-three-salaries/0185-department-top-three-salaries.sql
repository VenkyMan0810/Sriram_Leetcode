# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT b.name as Department,
    a.name as Employee,
    a.salary AS Salary,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY a.salary DESC) AS Salary_rank
    FROM Employee a
    JOIN Department b
    ON a.departmentId = b.id
)
SELECT Department, Employee, Salary
FROM CTE1
WHERE Salary_rank IN (1,2,3);

--  SELECT b.name as Department,
--     a.name as Employee,
--     a.salary,
--     DENSE_RANK() OVER (ORDER BY a.salary DESC) AS Salary_rank
--     FROM Employee a
--     JOIN Department b
--     ON a.departmentId = b.id