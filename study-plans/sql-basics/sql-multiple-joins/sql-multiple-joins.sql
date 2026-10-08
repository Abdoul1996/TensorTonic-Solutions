-- Returns: username, experiment_name, variant, revenue.
SELECT u.username, e.experiment_name, e.variant, c.revenue 
FROM users u
INNER JOIN experiment_assignments e ON u.id = e.user_id
INNER JOIN conversions c ON e.user_id = c.user_id
ORDER BY e.experiment_name ASC, c.revenue DESC, u.username ASC;
