MySQL doesn't allow directly nesting aggregate functions like `MAX` and `SUM`. This means you cannot write something like `SELECT MAX(SUM(column_name))` from your table.

Here are two common approaches to achieve the desired result:

**1. Subquery:**

This approach involves using a subquery to calculate the sum for each group and then applying the `MAX` function to the results:

```sql
SELECT MAX(total_value)
FROM (
  SELECT SUM(column_name) AS total_value
  FROM your_table
  GROUP BY group_by_column
) AS subquery;
```

In this example, `your_table` is replaced with your actual table name, `column_name` is the column you want to sum, and `group_by_column` is the column used for grouping. The subquery calculates the sum for each group and stores it in a temporary result set. The outer query then uses `MAX` to find the maximum value from the subquery's `total_value` column.

**2. Window Functions (MySQL 8.0+):**

If you're using MySQL version 8.0 or later, you can leverage window functions like `SUM` and `MAX` over window frames. This approach can be more efficient for certain queries:

```sql
SELECT
    group_by_column,
    MAX(SUM(column_name)) OVER (PARTITION BY group_by_column) AS max_sum
FROM your_table;
```

This query uses the `SUM` window function to calculate the running sum for each group defined by `group_by_column`. Then, the `MAX` window function finds the maximum value of the running sum within each group partition.