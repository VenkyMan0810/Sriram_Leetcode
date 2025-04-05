/* Write your T-SQL query statement below */
SELECT *
FROM Cinema
WHERE id % 2 = 1
AND DESCRIPTION <> 'boring'
ORDER BY rating DESC, id ASC;