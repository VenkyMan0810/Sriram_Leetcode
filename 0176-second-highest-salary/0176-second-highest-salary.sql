/* Write your T-SQL query statement below */
SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee
WHERE salary not in (
    SELECT MAX(salary) FROM Employee
)