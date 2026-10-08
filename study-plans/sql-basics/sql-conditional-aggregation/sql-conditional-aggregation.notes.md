Problem:

Each ticket has status open, in_progress, or closed. For each department, report total_tickets and the number in each status as open_count, in_progress_count, and closed_count. A status absent from a department has count zero. Return department, total_tickets, open_count, in_progress_count, and closed_count, in that column order, sorted by total_tickets descending and then department ascending.



Break Down:



Goal: Count each department tickets their status.



1. Count each department their tickets status 

1. sum(if status = open then 1 else 0 )
2. sum(if status = closed then 1 else 0 )
3. sum(if status = in_progress 1 else 0 )
2. 
3. Group by department

1. SUM of tikets and The nu
4. Count status