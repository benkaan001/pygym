
# Question

Find the number of employees working in the Admin department that joined in April or later.

## Expected Output

4

**Step 1: Filter by Department**

* We use a boolean indexing approach to select rows from the `worker` DataFrame where the 'department' column value is 'Admin'.


```py
filtered_by_department = worker[worker['department'] == 'Admin']
```

**Sample Output:**

| worker_id | first_name | last_name | department | joining_date |
| --------- | ---------- | --------- | ---------- | ------------ |
| 10        | John       | Doe       | Admin      | 2023-05-15   |
| 12        | Jane       | Smith     | Admin      | 2024-04-01   |

**Explanation:**

This creates a new DataFrame `filtered_by_department` containing only rows where the 'department' is 'Admin'.

**Step 2: Filter by Joining Date (Month >= 4)**

* We use the `dt.month` attribute to access the month component of the 'joining_date' column (assuming it's a datetime format).
* We then filter the DataFrame to include rows where the month value is greater than or equal to 4 (April).


```python
filtered_by_date = worker[worker['joining_date'].dt.month >= 4]
```

**Sample Output:**

| worker_id | first_name | last_name | department | joining_date |
| --------- | ---------- | --------- | ---------- | ------------ |
| 12        | Jane       | Smith     | Admin      | 2024-04-01   |
| 15        | Alice      | Young     | Sales      | 2024-05-10   |
| 18        | Mark       | Jones     | Marketing  | 2024-04-15   |

**Explanation:**

This creates a new DataFrame `filtered_by_date` containing rows where the joining month (from 'joining_date') is April (4) or later.

**Step 3: Combine Filters (Department & Joining Date)**

* We use the `&` operator for bitwise AND to combine the filtering conditions from both steps. This ensures we only select employees who meet both criteria (Admin department and April onwards joining date).


```python
filtered_workers = worker[(worker['joining_date'].dt.month >= 4) & (worker['department'] == 'Admin')]
```

**Sample Output:**

| worker_id | first_name | last_name | department | joining_date |
| --------- | ---------- | --------- | ---------- | ------------ |
| 12        | Jane       | Smith     | Admin      | 2024-04-01   |

**Explanation:**

This creates a new DataFrame `filtered_workers` containing only employees who joined the Admin department in April or later.

**Step 4: Count Matching Employees**

* We use the `shape[0]` attribute of the filtered DataFrame `filtered_workers` to get the number of rows (which represents the number of matching employees).


```python
number_of_employees = filtered_workers.shape[0]
print(f"Number of Employees (Admin Department, April onwards): {number_of_employees}")
```

**Sample Output:**

```python
Number of Employees (Admin Department, April onwards): 1
```
