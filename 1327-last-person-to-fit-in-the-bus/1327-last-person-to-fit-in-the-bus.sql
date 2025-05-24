# Write your MySQL query statement below
SELECT person_name 
FROM 
    (SELECT
    person_name, turn, 
    SUM(WEIGHT) OVER (ORDER BY turn) AS cumilative_weight
    FROM QUEUE) AS subq
WHERE cumilative_weight <= 1000
ORDER BY turn DESC
LIMIT 1;