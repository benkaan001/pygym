### Question:
Find matching hosts and guests pairs in a way that they are both of the same gender and nationality. Output the host ID and the guest ID of matched pairs.

### Solutions:

#### Solution:
```sql
SELECT DISTINCT
    h.host_id,
    g.guest_id
FROM
    airbnb_hosts h
JOIN
    airbnb_guests g
ON
    h.gender = g.gender
    AND h.nationality = g.nationality;
```

### Explanation:
- **Main Query**:
  - This query selects distinct pairs of host and guest IDs where both have the same gender and nationality.
  - It joins the `airbnb_hosts` and `airbnb_guests` tables based on the conditions that the gender and nationality of the host match those of the guest.

#### Alternative Solution:
```sql
SELECT DISTINCT
    h.host_id,
    g.guest_id
FROM
    airbnb_hosts h
JOIN
    airbnb_guests g
USING
    (gender, nationality);
```

### Explanation of Alternate Solution:
- This alternative solution achieves the same result using the `USING` keyword in the `JOIN` clause.
- It specifies that the join should be performed using columns with the same name (`gender` and `nationality`) in both tables.

### Sample Data:
Assuming the following structure and sample data for the `airbnb_hosts` and `airbnb_guests` tables:

**airbnb_hosts:**
| host_id | gender | nationality |
|---------|--------|-------------|
| 1       | Male   | USA         |
| 2       | Female | Canada      |
| 3       | Male   | USA         |
| 4       | Female | UK          |

**airbnb_guests:**
| guest_id | gender | nationality |
|----------|--------|-------------|
| 101      | Male   | USA         |
| 102      | Female | Canada      |
| 103      | Female | USA         |
| 104      | Male   | UK          |
| 105      | Male   | USA         |

### Expected Output:
| host_id | guest_id |
|---------|----------|
| 1       | 101      |
| 2       | 102      |
| 3       | 105      |
| 4       | 104      |

### Explanation of Expected Output:
- The pairs with host and guest IDs (1, 101), (2, 102), (3, 105), and (4, 104) have matching genders and nationalities.
- These pairs represent the matching hosts and guests in accordance with the conditions specified in the query.