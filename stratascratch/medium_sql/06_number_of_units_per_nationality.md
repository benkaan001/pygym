### Question:
Find the number of apartments per nationality that are owned by people under 30 years old. Output the nationality along with the number of apartments. Sort records by the apartments count in descending order.


#### Solution:
```sql
SELECT
    h.nationality,
    COUNT(DISTINCT u.unit_id) AS apartment_count
FROM
    airbnb_hosts h
JOIN
    airbnb_units u ON h.host_id = u.host_id
WHERE
    h.age < 30
    AND u.unit_type = 'Apartment'
GROUP BY
    h.nationality
ORDER BY
    apartment_count DESC;
```

### Explanation:
- **Main Query**:
  - This query retrieves the nationality of hosts and counts the number of apartments owned by hosts under 30 years old.
  - It uses a `JOIN` operation to combine data from the `airbnb_hosts` and `airbnb_units` tables based on the `host_id` column.
  - The `WHERE` clause filters hosts who are under 30 years old (`h.age < 30`) and units that are apartments (`u.unit_type = 'Apartment'`).
  - The `GROUP BY` clause groups the results by nationality to calculate the number of apartments per nationality.
  - Finally, the `ORDER BY` clause sorts the results by the apartment count in descending order.

### Sample Data:
Assuming the following structure and sample data for the `airbnb_hosts` and `airbnb_units` tables:

**airbnb_hosts:**
| host_id | nationality | age |
|---------|-------------|-----|
| 1       | USA         | 25  |
| 2       | Canada      | 28  |
| 3       | UK          | 32  |
| 4       | Germany     | 26  |
| 5       | USA         | 29  |

**airbnb_units:**
| unit_id | host_id | unit_type |
|---------|---------|-----------|
| 101     | 1       | Apartment |
| 102     | 1       | House     |
| 103     | 2       | Apartment |
| 104     | 3       | Apartment |
| 105     | 4       | Apartment |
| 106     | 4       | House     |
| 107     | 5       | Apartment |

### Expected Output:
| nationality | apartment_count |
|-------------|-----------------|
| USA         | 2               |
| Germany     | 1               |
| Canada      | 1               |

### Explanation of Expected Output:
- Hosts under 30 years old who own apartments are from the USA, Germany, and Canada.
- The USA has 2 apartments owned by hosts under 30, Germany has 1, and Canada has 1.

This query efficiently retrieves the number of apartments per nationality owned by people under 30 years old. The output is sorted by the apartment count in descending order, providing insights into the distribution of apartments among different nationalities.