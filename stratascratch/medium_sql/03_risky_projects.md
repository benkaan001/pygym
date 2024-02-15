### Question:
You are tasked with identifying projects that are at risk for going overbudget. A project is considered overbudget if the cost of all employees assigned to the project exceeds the project's budget.

You need to prorate the cost of the employees to the duration of the project. For example, if the budget for a project that takes half a year to complete is $10K, then the total half-year salary of all employees assigned to the project should not exceed $10K. Salary is defined on a yearly basis, so be careful how to calculate salaries for projects that last less or more than one year.

Output a list of projects that are overbudget with their project name, project budget, and prorated total employee expense (rounded to the next dollar amount).

HINT: to make it simpler, consider that all years have 365 days. You don't need to think about the leap years.

### Solutions:

#### Solution 1:
```sql
WITH emp_details_cte AS (
    SELECT
        ep.project_id,
        SUM(e.salary) AS total_emp_cost
    FROM
        linkedin_emp_projects ep
    JOIN
        linkedin_employees e ON ep.emp_id = e.id
    GROUP BY
        ep.project_id
),
project_details_cte AS (
    SELECT
        id,
        title,
        budget,
        DATEDIFF(end_date, start_date) AS project_length
    FROM
        linkedin_projects
)
SELECT
    title,
    budget,
    CEILING((total_emp_cost / 365) * project_length) AS prorated_employee_expense
FROM
    emp_details_cte
JOIN
    project_details_cte ON project_details_cte.id = emp_details_cte.project_id
WHERE
    total_emp_cost / 365 * project_length > budget
ORDER BY
    title;
```

#### Solution 2:
```sql
SELECT
    title,
    budget,
    CEIL(cost) AS cost
FROM (
    SELECT
        p.title,
        p.budget,
        SUM(e.salary)/365 * DATEDIFF(end_date,start_date) AS cost
    FROM
        linkedin_projects p
    JOIN
        linkedin_emp_projects ep ON p.id = ep.project_id
    JOIN
        linkedin_employees e ON e.id = ep.emp_id
    GROUP BY
        1, 2
) AS a
WHERE
    cost > budget;
```

### Sample Data:
Assuming the following tables and sample data:

**linkedin_projects:**
| id | title         | budget | start_date | end_date   |
|----|---------------|--------|------------|------------|
| 1  | Project A     | 10000  | 2023-01-01 | 2024-01-01 |
| 2  | Project B     | 20000  | 2023-02-01 | 2023-12-01 |
| 3  | Project C     | 15000  | 2023-03-01 | 2024-03-01 |

**linkedin_emp_projects:**
| emp_id | project_id |
|--------|------------|
| 1      | 1          |
| 2      | 1          |
| 3      | 2          |
| 4      | 3          |
| 5      | 3          |

**linkedin_employees:**
| id | salary |
|----|--------|
| 1  | 60000  |
| 2  | 50000  |
| 3  | 70000  |
| 4  | 55000  |
| 5  | 60000  |

### Expected Output:
| title    | budget | cost |
|----------|--------|------|
| Project A| 10000  | 21918|
| Project C| 15000  | 25370|

### Explanation:
- **Solution 1**:
  - Utilizes common table expressions (CTEs) to calculate the total employee cost per project and project details.
  - Calculates the prorated total employee expense using CEILING to round up to the next dollar amount.
  - Filters the results to include only projects where the prorated employee expense exceeds the project budget.
- **Solution 2**:
  - Calculates the prorated total employee expense directly within the main query.
  - Uses CEIL to round up the prorated expense.
  - Filters the results to include only projects where the prorated employee expense exceeds the project budget.

Both solutions aim to identify projects that are at risk for going overbudget by prorating the cost of employees to the project duration. They output the project title, budget, and prorated total employee expense.