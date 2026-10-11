Problem:

Assign consecutive row numbers starting at one within each segment. Higher engagement scores come first; equal scores are ordered by username ascending. Number every row separately, including tied scores. Return username, segment, engagement_score, and activity_rank, in that column order, sorted by segment ascending and then activity_rank ascending.



Break down:

1. Understand the goal — What am I being asked to calculate or return?

- The goal is return consecutive rwo numbers starting 1 each segment and sort them by engagement_score, and if its tie then user user_name
- Return username, segment, engagement score and activity rank based on their score rank

2. Identify the data — Which tables and columns do I need?

- cols: username, segment, engagement score and activity rank
- table: user_activity

3. Identify the operation — Filtering, grouping, joining, ranking, or aggregating?

- ROW_NUMBER(), PARTITION BY , ORDER BY

4. Break down the logic — What needs to happen, and in what order?

5. Define the output — Which columns and final sorting are required?

6. Write SQL and test — Check ties, NULLs, duplicates, and edge cases.