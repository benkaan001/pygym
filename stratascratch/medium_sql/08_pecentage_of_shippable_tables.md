### Question:
Find the percentage of shipable orders.
Consider an order is shipable if the customer's address is known.

### Solutions:

#### Solution:
```sql
WITH a AS (
    SELECT
        COUNT(*) AS shippable
    FROM
        orders
    JOIN
        customers ON orders.cust_id = customers.id
    WHERE
        address IS NOT NULL
), b AS (
    SELECT
        COUNT(*) AS total
    FROM
        orders
    JOIN
        customers ON orders.cust_id = customers.id
)
SELECT
    (shippable / total) * 100 AS percent_shipable
FROM
    a
JOIN
    b;
```

### Explanation:
- **Common Table Expressions (CTEs)**:
  - Two CTEs named `a` and `b` are created to count the number of shipable orders and the total number of orders, respectively.
  - CTE `a` counts shipable orders by joining the `orders` and `customers` tables on `cust_id` where the address is not null.
  - CTE `b` counts the total number of orders by joining the `orders` and `customers` tables on `cust_id`.

- **Main Query**:
  - The main query calculates the percentage of shipable orders by dividing the count of shipable orders (`shippable` from CTE `a`) by the total count of orders (`total` from CTE `b`).
  - It multiplies the result by 100 to get the percentage value.

#### Alternative Solution:
```sql
SELECT
    (COUNT(CASE WHEN address IS NOT NULL THEN 1 END) / COUNT(*)) * 100 AS percent_shipable
FROM
    orders
JOIN
    customers ON orders.cust_id = customers.id;
```

### Explanation of Alternate Solution:
- This alternative solution calculates the percentage of shipable orders using a single query without CTEs.
- It uses conditional aggregation to count shipable orders where the address is not null and divides it by the total count of orders.
- The result is multiplied by 100 to get the percentage value.

### Sample Data:
Assuming the following structure and sample data for the `orders` and `customers` tables:

**orders:**
| order_id | cust_id | status |
|----------|---------|--------|
| 1        | 101     | shipped|
| 2        | 102     | pending|
| 3        | 103     | shipped|
| 4        | 104     | shipped|
| 5        | 105     | pending|

**customers:**
| id  | address           |
|-----|-------------------|
| 101 | 123 Main St       |
| 102 | NULL              |
| 103 | 456 Elm St        |
| 104 | NULL              |
| 105 | 789 Oak St        |

### Expected Output:
| percent_shipable |
|------------------|
| 60.0             |

### Explanation of Expected Output:
- Out of the 5 orders, 3 have shipable addresses (orders with `order_id` 1, 3, and 4), and 2 do not (orders with `order_id` 2 and 5).
- Therefore, the percentage of shipable orders is (3 / 5) * 100 = 60.0%.