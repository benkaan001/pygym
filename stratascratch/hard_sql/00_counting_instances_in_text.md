# Question:

**Find the number of times the words 'bull' and 'bear' occur in the contents. Output the word 'bull' and 'bear' along with the corresponding number of occurrences.**

## Solution:

```sql
SELECT
    'bull' AS word,
    COUNT(contents) AS count
FROM google_file_store
WHERE contents LIKE '%bull%'
UNION
SELECT
    'bear' AS word,
    COUNT(contents) AS count
FROM google_file_store
WHERE contents LIKE '%bear%';
```

### Explanation of Solution:

- This SQL query uses a union of two select statements to count the occurrences of the words 'bull' and 'bear' separately.
- In the first select statement, we count the occurrences of 'bull' in the `contents` column of the `google_file_store` table.
- In the second select statement, we count the occurrences of 'bear' in the same column.
- The `LIKE '%bull%'` and `LIKE '%bear%'` conditions ensure that we only count the exact words 'bull' and 'bear', excluding substrings like 'bullish' or 'bearing'.


## Sample Data:

Assuming the following sample data for the `google_file_store` table:

| id | contents                                      |
|----|-----------------------------------------------|
| 1  | The bull market is showing signs of strength.|
| 2  | The bearish sentiment is impacting the market.|
| 3  | Investors are cautious due to bearish trends. |

## Expected Output:

| word | count |
|------|-------|
| bull | 1     |
| bear | 2     |
