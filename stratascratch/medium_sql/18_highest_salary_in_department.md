# Question:

**Find the employee with the highest salary per department. Output the department name, employee's first name, along with the corresponding salary.**

## Solution:

```sql
SELECT
    e1.department,
    e1.first_name AS employee_name,
    e1.salary
FROM employee e1
JOIN
(SELECT
    MAX(salary) AS max_salary,
    department
FROM employee
GROUP BY department) e2
ON e1.department = e2.department AND e1.salary = e2.max_salary;
```

### Explanation of Solution:

- This query selects the `department`, `first_name`, and `salary` columns from the `employee` table.
- It joins the `employee` table with a subquery that calculates the maximum salary (`max_salary`) for each department.
- The subquery `(SELECT MAX(salary) AS max_salary, department FROM employee GROUP BY department)` finds the maximum salary for each department.
- The join condition ensures that the result includes only employees whose salary matches the maximum salary for their respective department.

## Alternate Solution:

An alternative solution using the `ROW_NUMBER()` window function:

```sql
WITH ranked_employees AS (
    SELECT
        department,
        first_name AS employee_name,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employee
)
SELECT
    department,
    employee_name,
    salary
FROM ranked_employees
WHERE rnk = 1;
```

### Explanation of Alternate Solution:

- This alternative solution uses a Common Table Expression (CTE) named `ranked_employees`.
- Within the CTE, the `ROW_NUMBER()` window function is used to assign a rank to each employee within their department based on salary, with the highest salary receiving rank 1.
- The main query then selects employees where the rank is 1, effectively selecting the employee with the highest salary in each department.

## Sample Data:

Assuming the following sample data for the `employee` table:

| id | first_name | department | salary |
|----|------------|------------|--------|
| 1  | John       | HR         | 5000   |
| 2  | Alice      | HR         | 6000   |
| 3  | Bob        | IT         | 7000   |
| 4  | Emma       | IT         | 7500   |
| 5  | Sarah      | Finance    | 8000   |
| 6  | Mike       | Finance    | 8500   |

## Expected Output:

| department | employee_name | salary |
|------------|---------------|--------|
| HR         | Alice         | 6000   |
| IT         | Emma          | 7500   |
| Finance    | Mike          | 8500   |

### Explanation of Expected Output:

- In the sample data, Alice has the highest salary in the HR department, Emma has the highest salary in the IT department, and Mike has the highest salary in the Finance department.
- The expected output includes the department name, employee's first name, and corresponding salary for each department.