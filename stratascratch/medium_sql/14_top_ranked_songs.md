# Question:

Find songs that have ranked in the top position. Output the track name and the number of times it ranked at the top. Sort your records by the number of times the song was in the top position in descending order.

## Solution:

```sql
select
    trackname,
    sum(case when position = 1 then 1 else 0 end) as times_top1
from spotify_worldwide_daily_song_ranking spot
group by trackname
order by times_top1 desc
limit 3;
```

### Explanation of Solution:
- This query selects the track name and calculates the number of times each song ranked at the top position.
- The `sum(case when position = 1 then 1 else 0 end)` part of the query counts the number of times each track ranked at the top (position = 1).
- The `group by trackname` groups the results by the track name.
- The `order by times_top1 desc` sorts the records by the number of times each song was in the top position in descending order.
- The `limit 3` clause limits the output to the top 3 songs.

## Alternate Solution:

```sql
SELECT
    trackname,
    COUNT(*) AS times_top1
FROM spotify_worldwide_daily_song_ranking
WHERE position = 1
GROUP BY trackname
ORDER BY times_top1 DESC
LIMIT 3;
```

### Explanation of Alternate Solution:
- This alternative solution uses a simpler approach by directly filtering the rows where the position is 1 and counting the occurrences for each track.
- It selects the track name and calculates the number of times each song ranked at the top position.
- The `GROUP BY trackname` groups the results by the track name.
- The `ORDER BY times_top1 DESC` sorts the records by the number of times each song was in the top position in descending order.
- The `LIMIT 3` clause limits the output to the top 3 songs.

## Sample Data:
Assuming the following sample data for the `spotify_worldwide_daily_song_ranking` table:

| trackname        | position |
|------------------|----------|
| Song A           | 1        |
| Song A           | 2        |
| Song A           | 1        |
| Song B           | 1        |
| Song C           | 2        |
| Song B           | 1        |
| Song C           | 1        |
| ...              | ...      |

## Expected Output:
| trackname        | times_top1 |
|------------------|------------|
| Song A           | 2          |
| Song B           | 2          |
| Song C           | 1          |

### Explanation of Expected Output:
- Song A and Song B have each ranked at the top position twice.
- Song C has ranked at the top position once.
- The output is sorted by the number of times each song was in the top position in descending order.