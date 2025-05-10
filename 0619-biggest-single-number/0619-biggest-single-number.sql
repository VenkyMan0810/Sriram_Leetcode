# Write your MySQL query statement below

SELECT MAX(num) as num
FROM (
    SELECT num
    FROM myNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS sing
