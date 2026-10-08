Problem:

Summarize orders for customers who have placed at least two orders; exclude customers with fewer orders. Report their order count as total_orders and the sum of their amounts as total_spent. Return customer, total_orders, and total_spent, in that column order, sorted by total_spent descending. Customers with equal totals may appear in either order.



Break Down:



Goal: Summarize the customer orders who have at least placed 2 orders, the goal is to remove if its less than 2 orders.



1. Count the order of the customers AS total ORDERS 

1. filtering the orders at least 2 otherswise exclude that customers
2. Sum their amounts renamed Total spent of products
3. Return customers -&gt; total orders -&gt; total spent
4. Then sorted them by total spent DESC, if theres equal amounts it does not matter