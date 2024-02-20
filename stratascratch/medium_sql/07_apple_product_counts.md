### Question:
Find the number of Apple product users and the number of total users with a device and group the counts by language. Assume Apple products are only MacBook Pro, iPhone 5s, and iPad Air. Output the language along with the total number of Apple users and users with any device. Order your results based on the number of total users in descending order.

### Solutions:

#### Solution:
```sql
SELECT
    language,
    COUNT(DISTINCT
        CASE
            WHEN LOWER(device) IN ('macbook pro', 'iphone 5s', 'ipad air')
            THEN playbook_events.user_id
            ELSE NULL
        END)  AS n_apple_user,
    COUNT(DISTINCT playbook_events.user_id) AS n_total_users
FROM
    playbook_users
JOIN
    playbook_events ON playbook_events.user_id = playbook_users.user_id
GROUP BY
    language
ORDER BY
    n_total_users DESC;
```

### Explanation:
- **Main Query**:
  - This query retrieves the language of users and counts the number of Apple product users and the total number of users with any device.
  - It uses a `JOIN` operation to combine data from the `playbook_users` and `playbook_events` tables based on the `user_id` column.
  - The `CASE` statement categorizes users into Apple product users (`MacBook Pro`, `iPhone 5s`, and `iPad Air`) or users with other devices.
  - The `COUNT` function counts the distinct user IDs for Apple product users and total users for each language.
  - Finally, the results are grouped by language and ordered by the total number of users in descending order.

### Sample Data:
Assuming the following structure and sample data for the `playbook_users` and `playbook_events` tables:

**playbook_users:**
| user_id | language |
|---------|----------|
| 1       | English  |
| 2       | Spanish  |
| 3       | English  |
| 4       | German   |
| 5       | English  |

**playbook_events:**
| user_id | device       |
|---------|--------------|
| 1       | MacBook Pro  |
| 2       | iPhone 5s    |
| 3       | iPad Air     |
| 4       | Samsung S10  |
| 5       | MacBook Pro  |
| 5       | iPad Air     |

### Expected Output:
| language | n_apple_user | n_total_users |
|----------|--------------|---------------|
| English  | 3            | 4             |
| Spanish  | 1            | 1             |
| German   | 0            | 1             |

### Explanation of Expected Output:
- For the English language, there are 3 users with Apple products (`MacBook Pro`, `iPhone 5s`, and `iPad Air`) out of 4 total users.
- For the Spanish language, there is 1 user with an Apple product out of 1 total user.
- For the German language, there are no users with Apple products out of 1 total user.

This query efficiently calculates the number of Apple product users and total users with any device, grouped by language. The output is ordered by the number of total users in descending order, providing insights into the distribution of device users across different languages.