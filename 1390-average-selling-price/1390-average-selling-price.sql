/* Write your T-SQL query statement below */
SELECT a.product_id, ISNULL(ROUND(SUM(a.price * b.units)/CAST(SUM(b.units) AS FLOAT) ,2), 0) AS average_price
FROM Prices as a
LEFT JOIN UnitsSold as b
ON a.product_id = b.product_id
AND b.purchase_date BETWEEN a.start_date AND a.end_date 
GROUP BY a.product_id;