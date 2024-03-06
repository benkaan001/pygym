# Question:

**Find the highest target achieved by the employee or employees who work under the manager ID 13. Output the first name of the employee and the target achieved.**

## Solution:

```sql
SELECT
    first_name,
    target
FROM salesforce_employees
WHERE manager_id = 13 AND target =
    (SELECT
        MAX(target) AS max_target
    FROM salesforce_employees
    WHERE manager_id = 13);
```

### Explanation of Solution:

- This query selects the `first_name` and `target` columns from the `salesforce_employees` table.
- It filters the rows to include only those where `manager_id` is 13 and `target` is equal to the maximum target achieved by any employee under manager ID 13.
- The subquery `(SELECT MAX(target) AS max_target FROM salesforce_employees WHERE manager_id = 13)` calculates the maximum target achieved under manager ID 13.

## Alternate Solution:

An alternative solution using the `LIMIT` clause:

```sql
SELECT
    first_name,
    target
FROM salesforce_employees
WHERE manager_id = 13
ORDER BY target DESC
LIMIT 1;
```

### Explanation of Alternate Solution:

- This alternative solution selects the `first_name` and `target` columns from the `salesforce_employees` table.
- It orders the results by `target` in descending order, making the employee with the highest target appear first.
- The `LIMIT 1` ensures that only the top result is returned, representing the employee with the highest target.

## Sample Data:

Assuming the following sample data for the `salesforce_employees` table:

| id | first_name | manager_id | target |
|----|------------|------------|--------|
| 1  | John       | 13         | 1000   |
| 2  | Alice      | 13         | 1200   |
| 3  | Bob        | 13         | 800    |
| 4  | Emma       | 14         | 900    |

## Expected Output:

| first_name | target |
|------------|--------|
| Alice      | 1200   |

### Explanation of Expected Output:

- In the sample data, Alice has the highest target (1200) under manager ID 13.
- The expected output is Alice's first name and the corresponding target.