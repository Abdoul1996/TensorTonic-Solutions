-- Returns: customer, total_orders, total_spent.
SELECT customer, COUNT(*) AS total_orders, SUM(amount) AS total_spent
FROM orders
GROUP BY customer 
HAVING total_orders >= 2 
ORDER BY total_spent DESC;