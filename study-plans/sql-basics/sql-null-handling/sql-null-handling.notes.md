Problem:

Include only customers whose phone is not NULL. Set display_email to the stored email, or N/A when the email is NULL. Set status to active when deactivated_at is NULL and inactive otherwise. Return name, display_email, and status, in that column order, sorted by name ascending.



Breakdown:

1. We are removing customers who is phone is NULL 

1. WHERE phone IS NOT NULL
2. set display_email to the stored email or N/A(if they are NULL) 

1. COALESCE(email, N/A) AS display_email
3. set status to active (when deactivated_At is NULL) AND inactive otherwise 

1. CASE (

1. WHEN deactivated_at IS NULL THEN 'activate' ELSE 'inactivate' END
4. Return name, display_email and status sorted name ASC l