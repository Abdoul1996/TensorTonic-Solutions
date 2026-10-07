Problem:

Calculate each customer's total order amount, including customers without orders. An order's customer_id identifies the customer's id; customers with different ids remain separate even when their names match. Ignore NULL amounts and use zero when there is no non-null amount. Return name, city, and total_spent, in that column order, sorted by total_spent descending and then name ascending with NULL names last.



Break down: 



- Goal is to calculate total of each customer's order amount. 

- We can GROUP BY customer name
- Calculate the Amount they have spent
- Including customers without orders
- Customers table:

- has ID
- customer with different IDs in order remain (LEFT JOIN)
- Order table:

- has customer Id
- Sorted by total spent DESC and ASC by their name if there is equal