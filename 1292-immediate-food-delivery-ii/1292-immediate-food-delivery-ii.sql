# Write your MySQL query statement below
WITH RankedOrders AS (
    SELECT *, 
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS dateRank
    FROM Delivery
)
SELECT 
  ROUND(
    SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 
    / COUNT(*),
    2
  ) AS immediate_percentage
FROM RankedOrders
WHERE dateRank = 1;
