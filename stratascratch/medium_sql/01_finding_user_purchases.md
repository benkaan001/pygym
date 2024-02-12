### Question:
Write a query that'll identify returning active users.
A returning active user is a user that has made a second purchase within 7 days of any other of their purchases.
Output a list of `user_id` of these returning active users.

### Solution:
```sql
SELECT DISTINCT
    user_id
FROM
    amazon_transactions AS t1
WHERE
    EXISTS (
        SELECT 1
        FROM
            amazon_transactions AS t2
        WHERE
            t1.user_id = t2.user_id
            AND t2.created_at > t1.created_at
            AND DATEDIFF(t2.created_at, t1.created_at) <= 7
        LIMIT 1
    )
ORDER BY user_id;
```

### Solution:
```sql
SELECT
    DISTINCT t1.user_id
FROM amazon_transactions t1
JOIN amazon_transactions t2
ON t1.user_id = t2.user_id
WHERE t1.id <> t2.id AND DATEDIFF(t1.created_at, t2.created_at) BETWEEN 0 AND 7
ORDER BY t1.user_id;
```



### Sample Data:
Assuming the `amazon_transactions` table has the following structure and sample data:

| user_id | created_at          |
|---------|---------------------|
| 1       | 2024-02-01 08:00:00 |
| 2       | 2024-02-02 10:00:00 |
| 1       | 2024-02-05 12:00:00 |
| 3       | 2024-02-06 14:00:00 |
| 1       | 2024-02-10 16:00:00 |
| 4       | 2024-02-11 18:00:00 |
| 2       | 2024-02-15 20:00:00 |

### Expected Output:
| user_id |
|---------|
| 1       |
| 2       |

### Explanation:
1. **Main Query**: The outer query selects distinct `user_id` values from the `amazon_transactions` table aliased as `t1`.
2. **Subquery**: The `EXISTS` subquery checks if there exists another transaction (`t2`) for the same `user_id`, which occurred after the current transaction (`t1`) and within 7 days (`DATEDIFF(t2.created_at, t1.created_at) <= 7`).
3. **Distinct**: We use `DISTINCT` to ensure that each `user_id` appears only once in the result set, even if they meet the conditions for multiple transactions.
4. **Output**: The query outputs a list of `user_id` representing returning active users who made a second purchase within 7 days of any other purchase.

In the provided sample data, user 1 made purchases on 2024-02-01 and 2024-02-05, which are within 7 days of each other.
Similarly, user 2 made purchases on 2024-02-02 and 2024-02-15, also within 7 days of each other. Therefore, the expected output includes user IDs 1 and 2.