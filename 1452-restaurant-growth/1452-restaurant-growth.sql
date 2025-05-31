# Write your MySQL query statement below
-- SELECT DISTINCT
--     visited_on,
--     SUM(amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
--     ROUND(AVG(amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
-- FROM Customer
-- -- GROUP BY visited_on
-- LIMIT 1000000
-- OFFSET 6;


-- SELECT DISTINCT
--     visited_on,
--     SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,
--     ROUND(SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) / 7, 2) AS average_amount
-- FROM
--     Customer
-- LIMIT 1000000
-- OFFSET 6

SELECT DISTINCT
    visited_on,
    SUM(amount) OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,
    ROUND(SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) / 7, 2) AS average_amount
FROM Customer
LIMIT 1000000
OFFSET 6;
