### Question:
Find the top 5 businesses with the most reviews. Assume that each row has a unique business_id such that the total reviews for each business are listed on each row. Output the business name along with the total number of reviews and order your results by the total reviews in descending order.

### Solutions:

#### Solution:
```sql
SELECT
    name,
    SUM(review_count) AS review_count
FROM yelp_business
GROUP BY name
ORDER BY review_count DESC
LIMIT 5;
```

### Explanation of Solution:
- This solution retrieves the business name and sums up the review counts for each business using the `SUM()` function.
- The `GROUP BY` clause groups the rows by business name.
- The `ORDER BY` clause sorts the results in descending order based on the total review count.
- The `LIMIT 5` clause ensures that only the top 5 businesses with the highest review counts are returned.

### Alternate Solution:

#### Alternative Solution:
```sql
SELECT
    name,
    review_count
FROM (
    SELECT
        name,
        SUM(review_count) AS review_count,
        ROW_NUMBER() OVER (ORDER BY SUM(review_count) DESC) AS rn
    FROM yelp_business
    GROUP BY name
) AS ranked_businesses
WHERE rn <= 5;
```

### Explanation of Alternative Solution:
- This alternative solution uses a subquery to first calculate the total review count for each business and rank them using the `ROW_NUMBER()` window function.
- The outer query then selects the business name and review count from the subquery, filtering only the top 5 ranked businesses.
- While slightly more complex, this approach provides more flexibility and scalability, especially if you need to retrieve additional information or rank more than just the top 5 businesses.

### Sample Data:
Assuming the following sample data for the `yelp_business` table:

**yelp_business:**
| business_id | name             | review_count |
|-------------|------------------|--------------|
| 1           | Business A       | 100          |
| 2           | Business B       | 150          |
| 3           | Business C       | 80           |
| 4           | Business D       | 200          |
| 5           | Business E       | 120          |
| ...         | ...              | ...          |

### Expected Output:
| name        | review_count |
|-------------|--------------|
| Business D  | 200          |
| Business B  | 150          |
| Business E  | 120          |
| Business A  | 100          |
| Business C  | 80           |

### Explanation of Expected Output:
- The query identifies the top 5 businesses with the highest total review counts.
- The businesses are ordered by their total review counts in descending order, and only the top 5 are returned.