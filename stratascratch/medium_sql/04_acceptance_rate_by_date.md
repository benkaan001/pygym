### Question:
What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date the request was sent. Order by the earliest date to latest.

Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver) that's logged in the table with action = 'sent'. If the request is accepted, the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.

#### Solution:
```sql
WITH approver_cte AS (
    SELECT *
    FROM fb_friend_requests
    WHERE action='accepted'
),
sender_cte AS (
    SELECT *
    FROM fb_friend_requests
    WHERE action='sent'
)
SELECT
    sender_cte.date,
    COUNT(approver_cte.user_id_receiver) / COUNT(sender_cte.user_id_sender) AS acceptance_rate
FROM
    approver_cte
RIGHT JOIN
    sender_cte ON approver_cte.user_id_sender = sender_cte.user_id_sender
              AND approver_cte.user_id_receiver = sender_cte.user_id_receiver
GROUP BY
    date
ORDER BY
    date;
```

### Explanation:
- **Common Table Expressions (CTEs)**:
  - Two CTEs named `approver_cte` and `sender_cte` are created to filter friend requests based on their action types.
  - `approver_cte` selects all friend requests where the action is 'accepted'.
  - `sender_cte` selects all friend requests where the action is 'sent'.

- **Main Query**:
  - The main query joins the `approver_cte` and `sender_cte` based on the sender and receiver user IDs.
  - It calculates the friend acceptance rate by dividing the count of accepted requests by the count of sent requests for each date.
  - The `RIGHT JOIN` ensures that all sent requests are included in the calculation, even if there are no corresponding accepted requests.

- **Grouping and Ordering**:
  - The results are grouped by date to calculate the acceptance rate for each date.
  - They are then ordered by date in ascending order to present the acceptance rates from the earliest date to the latest.

### Sample Data:
Assuming the following structure and sample data for the `fb_friend_requests` table:

| user_id_sender | user_id_receiver | action    | date       |
|----------------|------------------|-----------|------------|
| 1              | 2                | sent      | 2023-01-01 |
| 2              | 1                | accepted  | 2023-01-02 |
| 3              | 4                | sent      | 2023-01-03 |
| 5              | 3                | sent      | 2023-01-03 |
| 4              | 3                | sent      | 2023-01-04 |

### Expected Output:
| date       | acceptance_rate |
|------------|-----------------|
| 2023-01-01 | 0.5             |
| 2023-01-03 | 0               |
| 2023-01-04 | 0               |

### Explanation of Expected Output:
- On '2023-01-01', there is 1 sent request and 1 accepted request. So, the acceptance rate is 1/1 = 0.5.
- On '2023-01-03' and '2023-01-04', there are only sent requests but no accepted requests. So, the acceptance rate is 0/1 = 0 for both dates.

