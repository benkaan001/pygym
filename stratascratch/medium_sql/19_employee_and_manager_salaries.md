# Question:

**Find employees who are earning more than their managers. Output the employee's first name along with the corresponding salary.**

## Solution:

```sql
SELECT
    employees.first_name AS employee_name,
    employees.salary AS employee_salary
FROM employee employees
JOIN employee managers
ON employees.manager_id = managers.id
WHERE employees.salary > managers.salary;
```

### Explanation of Solution:

- This SQL query selects the `first_name` and `salary` columns from the `employee` table for employees who earn more than their managers.
- It performs a self-join on the `employee` table, matching each employee with their respective manager based on the `manager_id` field.
- The `WHERE` clause filters the result to include only those employees whose salary is greater than their manager's salary.

## Alternate Solution:

An alternative solution using a correlated subquery:

```sql
SELECT
    first_name AS employee_name,
    salary AS employee_salary
FROM employee e
WHERE salary > (SELECT m.salary FROM employee m WHERE e.manager_id = m.id);
```

### Explanation of Alternate Solution:

- This alternative solution uses a correlated subquery within the `WHERE` clause.
- For each row in the `employee` table (aliased as `e`), the subquery `(SELECT m.salary FROM employee m WHERE e.manager_id = m.id)` retrieves the salary of the corresponding manager.
- The main query then filters out employees whose salary is greater than that of their manager.

## Sample Data:

Assuming the following sample data for the `employee` table:

| id | first_name | salary | manager_id |
|----|------------|--------|------------|
| 1  | John       | 5000   | NULL       |
| 2  | Alice      | 6000   | 1          |
| 3  | Bob        | 7000   | 1          |
| 4  | Emma       | 7500   | 2          |
| 5  | Sarah      | 8000   | 3          |
| 6  | Mike       | 8500   | 3          |

## Expected Output:

| employee_name | employee_salary |
|---------------|-----------------|
| Emma          | 7500            |
| Sarah         | 8000            |
| Mike          | 8500            |

### Explanation of Expected Output:

- In the sample data, Emma, Sarah, and Mike earn more than their respective managers (John, Alice, and Bob).
- The expected output includes the first name and salary of each employee who earns more than their manager.
