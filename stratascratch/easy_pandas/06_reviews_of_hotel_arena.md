## Counting Reviews by Score for 'Hotel Arena'

This solution addresses the task of finding the number of reviews each score received by 'Hotel Arena'. Here's a breakdown of the steps involved:

**Step 1: Filter Reviews for 'Hotel Arena'**

* We use `.query("hotel_name == 'Hotel Arena'")` to filter the `hotel_reviews` DataFrame and select only rows where the 'hotel_name' is 'Hotel Arena'.
* We then select the relevant columns (`reviewer_score` and `hotel_name`) using `[['reviewer_score', 'hotel_name']]`.



```python
filtered_df = hotel_reviews.query("hotel_name == 'Hotel Arena'")[['reviewer_score', 'hotel_name']]
```

**Explanation:**

This step creates a new DataFrame (`filtered_df`) containing reviews specifically for 'Hotel Arena' and keeps only the 'reviewer_score' and 'hotel_name' columns for this task.

**Step 2: Group by Score and Count Reviews**

* We use `.groupby('reviewer_score')` to group the filtered DataFrame (`filtered_df`) by the 'reviewer_score' column. This creates groups for each unique review score.
* We then use `.count()` on the grouped data to count the number of reviews within each score group. The result (`grouped_df`) is a Series containing review scores as the index and review counts as the values.


```python
grouped_df = filtered_df.groupby('reviewer_score').count()
```

**Explanation:**

This step categorizes the reviews based on the reviewer score and then calculates the number of reviews given for each score. The output is a Series where the index represents the review score and the values represent the number of reviews for that score (specifically for 'Hotel Arena').

**Step 3: Print the Results (Series)**

* While not explicitly mentioned in the provided steps, you can print `grouped_df` to view the Series containing the review score counts.


```python
print(grouped_df)
```

**Sample Output:**

```
reviewer_score
1.0    2
2.0    5
3.0    3
4.0    4
5.0    1
dtype: int64
```

