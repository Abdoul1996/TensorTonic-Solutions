-- Write your SQL query hereS

SELECT 
    name,
    salary
    FROM employees WHERE department IN ('Engineering', 'Marketing') AND salary > 70000