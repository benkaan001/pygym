### Question:
Rank guests based on the total number of messages they've exchanged with any of the hosts. Guests with the same number of messages as other guests should have the same rank. Do not skip rankings if the preceding rankings are identical. Output the rank, guest ID, and number of total messages they've sent. Order by the highest number of total messages first.

#### Solution:
```sql
SELECT
    id_guest,
    DENSE_RANK() OVER (ORDER BY SUM(n_messages) DESC) AS ranks,
    SUM(n_messages) AS messages
FROM
    airbnb_contacts
GROUP BY
    id_guest
ORDER BY
    messages DESC;
```

### Explanation:
- **Main Query**:
  - This query calculates the rank of each guest based on the total number of messages they've exchanged with any of the hosts.
  - It uses the `DENSE_RANK()` window function to assign ranks to guests based on the descending order of the sum of messages.
  - The query also calculates the total number of messages sent by each guest using the `SUM()` function.

- **Grouping and Ordering**:
  - The results are grouped by `id_guest` to calculate the total number of messages sent by each guest.
  - The results are then ordered by the total number of messages in descending order to rank guests with the highest number of messages first.

### Sample Data:
Assuming the following structure and sample data for the `airbnb_contacts` table:

| id_guest | id_host | n_messages |
|----------|---------|------------|
| 1        | 101     | 10         |
| 1        | 102     | 5          |
| 2        | 101     | 8          |
| 3        | 102     | 12         |
| 3        | 103     | 15         |
| 4        | 101     | 6          |
| 4        | 103     | 9          |

### Expected Output:
| id_guest | ranks | messages |
|----------|-------|----------|
| 3        | 1     | 27       |
| 1        | 2     | 15       |
| 4        | 3     | 15       |
| 2        | 4     | 8        |

### Explanation of Expected Output:
- Guest with `id_guest = 3` has sent the highest total number of messages (27), so it gets the highest rank (1).
- Guests with `id_guest = 1` and `id_guest = 4` have sent the same total number of messages (15), so they get the same rank (2 and 3, respectively).
- Guest with `id_guest = 2` has sent the lowest total number of messages (8), so it gets the lowest rank (4).