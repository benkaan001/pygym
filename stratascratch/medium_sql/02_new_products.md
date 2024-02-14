### Question:
You are given a table of product launches by company by year. Write a query to count the net difference between the number of products companies launched in 2020 with the number of products companies launched in the previous year. Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.

### Solutions:

#### Solution 1:
```sql
WITH 2019_launch_cte AS (
    SELECT
        company_name,
        COUNT(product_name) AS product_count
    FROM
        car_launches
    WHERE
        year = 2019
    GROUP BY
        company_name
),
2020_launch_cte AS (
    SELECT
        company_name,
        COUNT(product_name) AS product_count
    FROM
        car_launches
    WHERE
        year = 2020
    GROUP BY
        company_name
)
SELECT
    2020_launch_cte.company_name,
    2020_launch_cte.product_count - 2019_launch_cte.product_count AS total_launch
FROM
    2020_launch_cte
JOIN
    2019_launch_cte ON 2020_launch_cte.company_name = 2019_launch_cte.company_name;
```

#### Solution 2:
```sql
SELECT
    company_name,
    COUNT(CASE WHEN (year = 2020) THEN 1 END) - COUNT(CASE WHEN (year = 2019) THEN 1 END) AS total_launch
FROM
    car_launches
GROUP BY
    company_name;
```

#### Solution 3:
```sql
SELECT
    company_name,
    SUM(year = 2020) - SUM(year = 2019) AS net_diff
FROM
    car_launches
GROUP BY
    company_name
ORDER BY
    company_name;
```

### Sample Data:
Assuming the `car_launches` table has the following structure and sample data:

| company_name | product_name | year |
|--------------|--------------|------|
| Company A    | Product 1    | 2019 |
| Company A    | Product 2    | 2019 |
| Company A    | Product 3    | 2020 |
| Company B    | Product 4    | 2019 |
| Company B    | Product 5    | 2020 |
| Company C    | Product 6    | 2020 |

### Expected Output:
| company_name | total_launch |
|--------------|--------------|
| Company A    | 1            |
| Company B    | 1            |
| Company C    | 1            |

### Explanation:
- **Solution 1**: This solution uses common table expressions (CTEs) to calculate the number of product launches for each company in 2019 and 2020 separately. It then joins these CTEs to calculate the net difference in product launches between the two years.
- **Solution 2**: This solution uses conditional aggregation with `CASE` statements to count the number of product launches for each company in 2019 and 2020, and then calculates the net difference.
- **Solution 3**: This solution also uses conditional aggregation, but instead of `CASE` statements, it leverages the fact that in SQL, boolean expressions can be treated as integers (0 for false, 1 for true). It sums the boolean expressions for each year and subtracts them to calculate the net difference.