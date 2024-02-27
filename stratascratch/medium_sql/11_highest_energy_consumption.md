### Question:
Find the date with the highest total energy consumption from the Meta/Facebook data centers. Output the date along with the total energy consumption across all data centers.

### Solutions:

```sql
WITH union_table AS (
    SELECT date, consumption FROM fb_eu_energy
    UNION
    SELECT date, consumption FROM fb_asia_energy
    UNION
    SELECT date, consumption FROM fb_na_energy
), combined_table AS (
    SELECT
        date,
        SUM(consumption) AS consumption
    FROM union_table
    GROUP BY date
)
SELECT * FROM combined_table WHERE consumption = (SELECT MAX(consumption) FROM combined_table);
```

### Explanation:
- **Union Tables**:
  - The `union_table` CTE combines the energy consumption data from three separate tables (`fb_eu_energy`, `fb_asia_energy`, and `fb_na_energy`) into a single table using the `UNION` operator.
- **Combined Table**:
  - The `combined_table` CTE calculates the total energy consumption for each date by summing the consumption across all data centers.
- **Main Query**:
  - The main query selects all records from the `combined_table` where the consumption is equal to the maximum consumption found in the dataset.
  - This effectively identifies the date(s) with the highest total energy consumption across all data centers.

### Alternative Solution:
```sql
WITH combined_table AS (
    SELECT
        date,
        SUM(consumption) AS consumption
    FROM (
        SELECT date, consumption FROM fb_eu_energy
        UNION ALL
        SELECT date, consumption FROM fb_asia_energy
        UNION ALL
        SELECT date, consumption FROM fb_na_energy
    ) AS union_table
    GROUP BY date
)
SELECT * FROM combined_table
WHERE consumption = (SELECT MAX(consumption) FROM combined_table);
```

### Explanation of Alternate Solution:
- This alternative solution achieves the same result but uses `UNION ALL` instead of `UNION` in the `union_table` CTE.
- Unlike `UNION`, `UNION ALL` includes all records from each table, including duplicates. Since the data is being aggregated later in the `combined_table`, there is no need to remove duplicates, making `UNION ALL` potentially faster.
- The rest of the query structure remains the same as the main solution.

### Sample Data:
Assuming the following sample data for the `fb_eu_energy`, `fb_asia_energy`, and `fb_na_energy` tables:

**fb_eu_energy:**
| date       | consumption |
|------------|-------------|
| 2023-01-01 | 500         |
| 2023-01-02 | 600         |
| 2023-01-03 | 700         |
| ...        | ...         |

**fb_asia_energy:**
| date       | consumption |
|------------|-------------|
| 2023-01-01 | 800         |
| 2023-01-02 | 900         |
| 2023-01-03 | 1000        |
| ...        | ...         |

**fb_na_energy:**
| date       | consumption |
|------------|-------------|
| 2023-01-01 | 1200        |
| 2023-01-02 | 1300        |
| 2023-01-03 | 1400        |
| ...        | ...         |

### Expected Output:
| date       | consumption |
|------------|-------------|
| 2023-01-03 | 3100        |
