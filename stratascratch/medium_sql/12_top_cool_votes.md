### Question:
Find the review_text that received the highest number of 'cool' votes. Output the business name along with the review text with the highest number of 'cool' votes.

### Solutions:

#### Solution 1:
```sql
SELECT business_name, review_text
FROM yelp_reviews
WHERE cool = (SELECT max(cool) FROM yelp_reviews);
```

**Explanation:**

1. **`SELECT business_name, review_text`:** This clause selects the `business_name` and `review_text` columns from the `yelp_reviews` table.
2. **`FROM yelp_reviews`:** This clause specifies the table from which data will be retrieved.
3. **`WHERE cool = (SELECT max(cool) FROM yelp_reviews)`:** This clause filters the results to only include reviews where the "cool" vote count is equal to the maximum "cool" vote count across all reviews.
    - The subquery:
        - **`SELECT max(cool) FROM yelp_reviews`:** This subquery finds the maximum value for the "cool" vote count in the entire table.
    - By comparing the "cool" vote count of each review with the maximum value, we ensure we only select the review with the highest number of votes.

#### Solution 2:

This solution utilizes a single table scan and window function (available in MySQL 8.0+):

```sql
SELECT business_name, review_text
FROM yelp_reviews
WHERE cool = RANK() OVER (ORDER BY cool DESC) = 1;
```

**Explanation:**

1. **`SELECT business_name, review_text`:** This clause selects the `business_name` and `review_text` columns from the `yelp_reviews` table.
2. **`FROM yelp_reviews`:** This clause specifies the table from which data will be retrieved.
3. **`WHERE cool = RANK() OVER (ORDER BY cool DESC) = 1`:** This clause filters the results to only include reviews where the "cool" vote count is equal to 1.
    - **`RANK() OVER (ORDER BY cool DESC)`:** This window function assigns a rank (starting from 1) to each review based on "cool" vote count in descending order.
    - By comparing the "cool" vote count of each review with the rank of 1, we ensure we only select the review with the highest number of votes.

### Sample Data:
Assuming the following structure and sample data for the `yelp_reviews` table:

**yelp_reviews:**
| business_name | review_text                               | cool |
|---------------|-------------------------------------------|------|
| Business A    | This place is amazing!                    | 10   |
| Business A    | Great food and atmosphere.                | 5    |
| Business B    | Excellent service.                        | 8    |
| Business C    | Awesome experience, highly recommended.   | 12   |
| ...           | ...                                       | ...  |

### Expected Output:
| business_name | review_text                               |
|---------------|-------------------------------------------|
| Business C    | Awesome experience, highly recommended.   |

### Explanation of Expected Output:
- The query identifies the review with the highest number of 'cool' votes, which is associated with the business name "Business C".
- The review text "Awesome experience, highly recommended." received the highest number of 'cool' votes. Therefore, it is the output.
