Problem:

Summarize sales by category. The amount is present for every sale, but discount may be NULL. Count every sale in total_sales, sum amounts into total_revenue, and average only non-NULL discounts into avg_discount, rounded to two decimal places. If a category has no non-NULL discounts, its avg_discount is NULL. Return category, total_sales, total_revenue, and avg_discount, in that column order, sorted by total_revenue descending and then category ascending.



BREAK DOWN:



Goal: Summarize the sales of the category by their sum, average and rounded to two decimals places 



1. Count every category sale AS total_sales 

1. COUNT(*)
2. Total amount of each category product 

1. SUM(amount)
3. average of the discounts only non-nul Renamed avg_discount then rounded two decimal places 

1. avg(discount)

1. If category has no non-null discounts keep the average as NULL
4. Return category -&gt; total sales -&gt; total_revenue &gt; avg_discount and then SORT by total_revenue DESC and then category ASC