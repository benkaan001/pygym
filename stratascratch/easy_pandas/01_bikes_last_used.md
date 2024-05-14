# Question

Find the last time each bike was in use. Output both the bike number and the date-timestamp of the bike's last use (i.e., the date-time the bike was returned). Order the results by bikes that were most recently used.

## Expected Output

| bike_number | last_used           |
| ----------- | ------------------- |
| W01278      | 2012-03-31 19:28:00 |
| W01097      | 2012-03-31 15:37:00 |
| W00270      | 2012-03-31 12:10:00 |
| W01006      | 2012-03-31 10:44:00 |
| W01242      | 2012-03-31 09:24:00 |

## Steps

**Step 1: Group by Bike Number and Find Maximum End Time**

```python
# Group the DataFrame by 'bike_number'
grouped_by_bike = dc_bikeshare_q1_2012.groupby("bike_number")

# Find the maximum 'end_time' (last used time) for each bike group
max_end_time_per_bike = grouped_by_bike["end_time"].max()
```

**Explanation:**

* We use `groupby("bike_number")` to create groups of rows where the `bike_number` is the same. This allows us to perform operations on each bike individually.
* Within each group, we use `.max()` on the `end_time` column to find the latest `end_time` (last return time) for that particular bike.

**Sample Output:**

```python
bike_number
1001           2012-01-31 23:59:00
1002           2012-01-25 17:30:00
1003           2012-01-29 12:00:00
# ... (other bikes and their last used times)
```

* This output shows a Series where the index is the `bike_number` and the values are the corresponding maximum `end_time` for each bike.

**Step 2: Create a DataFrame with the Maximum End Time**

```python
# Convert the Series from Step 1 into a DataFrame
last_used_df = max_end_time_per_bike.to_frame("last_used")
```

**Explanation:**

* We use `.to_frame("last_used")` to convert the Series from Step 1 into a DataFrame. This creates a new DataFrame with a single column named "last_used" that contains the maximum `end_time` for each bike.

**Sample Output:**

```python
           last_used
bike_number
1001  2012-01-31 23:59:00
1002  2012-01-25 17:30:00
1003  2012-01-29 12:00:00
# ... (other bikes and their last used times)
```

* Now we have a DataFrame with the `bike_number` as the index and a new column named "last_used" that holds the last used time for each bike.

**Step 3: Reset the Index to Include Bike Number as a Column**

```python
# Reset the index to include 'bike_number' as a column in the DataFrame
last_used_df = last_used_df.reset_index()
```

**Explanation:**

* By default, `groupby` operations use the grouping column(s) as the index of the resulting Series or DataFrame. Here, the index is `bike_number`.
* `.reset_index()` converts the index into a regular column named after the former index. This makes it easier to work with the data in the DataFrame.

**Sample Output:**

```python
  bike_number           last_used
0         1001  2012-01-31 23:59:00
1         1002  2012-01-25 17:30:00
2         1003  2012-01-29 12:00:00
# ... (other bikes and their last used times)
```

* Now we have a DataFrame with two columns: "bike_number" and "last_used", making it easier to analyze the data.

**Step 4: Sort by Last Used Time (Descending)**

```python
# Sort the DataFrame by 'last_used' in descending order (most recent first)
last_used_df = last_used_df.sort_values(by="last_used", ascending=False)
```

**Explanation:**

* `.sort_values(by="last_used", ascending=False)` sorts the DataFrame by the "last_used"
