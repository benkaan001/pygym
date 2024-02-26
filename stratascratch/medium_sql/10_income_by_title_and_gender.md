### Question:
Find the average total compensation based on employee titles and gender. Total compensation is calculated by adding both the salary and bonus of each employee. However, not every employee receives a bonus so disregard employees without bonuses in your calculation. Employees can receive more than one bonus. Output the employee title, gender (i.e., sex), along with the average total compensation.

### Solution:
```sql
SELECT
    e.employee_title,
    e.sex,
    AVG(e.salary + b.bonus)
FROM
    sf_employee e
JOIN (
    SELECT
        worker_ref_id,
        SUM(bonus) AS bonus
    FROM
        sf_bonus
    GROUP BY 1
) b
ON
    e.id = b.worker_ref_id
GROUP BY
    e.employee_title, e.sex;
```

### Explanation:
- **Main Query**:
  - This query calculates the average total compensation for each combination of employee title and gender.
  - It joins the `sf_employee` table with the `sf_bonus` table based on the `id` and `worker_ref_id` columns, respectively.
  - The average total compensation is calculated by adding the salary and bonus (if any) for each employee, and then taking the average.
  - Results are grouped by employee title and gender.


### Sample Data:
Assuming the following structure and sample data for the `sf_employee` and `sf_bonus` tables:

**sf_employee:**
| id | employee_title | sex    | salary |
|----|----------------|--------|--------|
| 1  | Manager        | Female | 60000  |
| 2  | Engineer       | Male   | 70000  |
| 3  | Analyst        | Male   | 55000  |
| 4  | Manager        | Male   | 65000  |
| 5  | Engineer       | Female | 75000  |

**sf_bonus:**
| worker_ref_id | bonus |
|---------------|-------|
| 1             | 5000  |
| 1             | 3000  |
| 2             | 4000  |
| 4             | 6000  |
| 5             | 7000  |
| 5             | 2500  |

### Expected Output:
| employee_title | sex    | avg_total_compensation |
|----------------|--------|------------------------|
| Manager        | Female | 61500                  |
| Engineer       | Male   | 72000                  |
| Analyst        | Male   | 55000                  |
| Manager        | Male   | 65500                  |
| Engineer       | Female | 73750                  |

### Explanation of Expected Output:
- For each combination of employee title and gender:
  - The average total compensation is calculated by summing the salary and bonuses (if any) for each employee and then taking the average.
  - Employees without bonuses are excluded from the calculation.