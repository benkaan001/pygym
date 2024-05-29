## Counting Abigail Breslin's Oscar Nominations

This solution calculates the number of Oscar nominations received by Abigail Breslin. Here's a breakdown of the steps:

**Step 1: Filter Nominees by Name**

- We use `oscar_nominees[oscar_nominees.nominee == 'Abigail Breslin']` to filter the `oscar_nominees` DataFrame and select only rows where the 'nominee' column value is 'Abigail Breslin'. This creates a new DataFrame (`filtered_df`) containing just Abigail Breslin's nominations.

   ```python
   filtered_df = oscar_nominees[oscar_nominees.nominee == 'Abigail Breslin']
   ```

**Explanation:**

This step isolates the rows relevant to Abigail Breslin from the larger DataFrame containing all nominees.

**Step 2: Count the Rows (Number of Nominations)**

- We use `.shape[0]` on the filtered DataFrame (`filtered_df`) to retrieve the number of rows. This represents the number of times Abigail Breslin's name appears in the 'nominee' column, indicating the total number of her Oscar nominations.

   ```python
   filtered_df.shape[0]
   ```

**Explanation:**

The `.shape` attribute provides a tuple containing the DataFrame dimensions (rows, columns). By accessing `.shape[0]`, we get the number of rows, which corresponds to the number of nominations in this case. The result is then printed in a clear message.

**Sample Output:**

```
1
```

**Note:**

This assumes the `oscar_nominees` DataFrame has a 'nominee' column containing the names of nominees and potentially other relevant information.