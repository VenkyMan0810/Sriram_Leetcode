# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price FROM Product AS p
RIGHT JOIN Sales as S
ON s.product_id = p.product_id;