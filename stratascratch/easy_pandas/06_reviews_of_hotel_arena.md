## Counting Reviews by Score for 'Hotel Arena' (Explicit Columns)


**Steps:**

1. **Filter Reviews for 'Hotel Arena'**

   - We use `.query("hotel_name == 'Hotel Arena'")` to filter the `hotel_reviews` DataFrame and select only rows where the 'hotel_name' is 'Hotel Arena'.

   ```python
   filtered_df = hotel_reviews.query("hotel_name == 'Hotel Arena'")
   ```

   **Explanation:**

   This step creates a new DataFrame (`filtered_df`) containing reviews specifically for 'Hotel Arena'.

2. **Group by Score and Count (with Hotel Name)**

   - We use `.groupby(['reviewer_score', 'hotel_name'])` to group the filtered DataFrame (`filtered_df`) by both the 'reviewer_score' and 'hotel_name' columns. This ensures each score is counted specifically for 'Hotel Arena'.
   - `.size()` calculates the number of reviews within each group (score and hotel name combination).
   - `.to_frame(name='n_reviews')` converts the result into a DataFrame with a column named 'n_reviews' containing the review counts.

   ```python
   grouped_df = filtered_df.groupby(['reviewer_score', 'hotel_name']).size().to_frame(name='n_reviews')
   ```

   **Explanation:**

   This step groups the reviews based on the reviewer score **and** explicitly includes the hotel name in the grouping. The `.size()` function then counts the occurrences within each group, resulting in a Series with reviewer score and hotel name as the index, and the corresponding number of reviews ('n_reviews') as the values.

3. **Reset Index for Columns (Optional)**

   - While not strictly necessary for this specific task, `.reset_index()` transforms the multi-level index (from grouping) into regular columns within the DataFrame (`grouped_df`). This can improve readability, especially when working with the DataFrame later.

   ```python
   grouped_df = grouped_df.reset_index()
   ```

   **Explanation:**

   This step, although optional, creates a more conventional DataFrame structure by incorporating the grouping variables ('reviewer_score' and 'hotel_name') as regular columns alongside the 'n_reviews' column.

**Sample Output:**

| reviewer_score | hotel_name | n_reviews |
|---|---|---|
| 3.8             | Hotel Arena | 1         |
| 4.2             | Hotel Arena | 4         |
| 4.6             | Hotel Arena | 5         |
| 5.4             | Hotel Arena | 8         |
| 5.8             | Hotel Arena | 2         |
