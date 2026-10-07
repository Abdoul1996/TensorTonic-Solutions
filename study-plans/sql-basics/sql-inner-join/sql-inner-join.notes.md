problem:

An employee's dept_id identifies the department. Include each employee with a matching department and exclude employees without one. Return name, salary, and dept_name, in that column order, sorted by employee name ascending, with NULL names last.



- **What do I need to return?** → `SELECT`

- name, salary, and dept_name
- **Where does the data come from?** → `FROM`

- departments and employees
- Where they have an intersection between two tables:

- depart_id for department and Id employees
- **Which rows should I keep/remove?** → `WHERE`

- We are removing rows that do not match IDs
- **Does it say "for each" or "per"?** → probably `GROUP BY`
- **What calculation do I need?** → `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, etc.

- We are using INNER JOIN to find the intersections of both tables
- **How should the result be sorted/limited?** → `ORDER BY`, `LIMIT`

- return name, salary and dept_name ORDER THEM