# Question:

Find the Olympics with the highest number of athletes. The Olympics game is a combination of the year and the season, and is found in the 'games' column. Output the Olympics along with the corresponding number of athletes.

## Solution:

```sql
select
    games,
    athletes_count
from
    (select
        games,
        count(distinct name) as athletes_count,
        row_number() over (order by count(distinct name) desc ) as rk
    from olympics_athletes_events
    group by games
    ) t
where rk = 1;
```

### Explanation of Solution:
- This query selects the Olympics game (`games`) and calculates the number of distinct athletes (`athletes_count`) for each game.
- The inner query groups the data by the Olympics game and counts the number of distinct athletes.
- The `row_number() over (order by count(distinct name) desc)` function assigns a rank to each row based on the count of distinct athletes, in descending order.
- The outer query selects the Olympics game and the corresponding athlete count where the rank is 1, indicating the Olympics with the highest number of athletes.

## Alternate Solution:

```sql
select
    games,
    count(distinct name) as athletes_count
from olympics_athletes_events
group by games
order by athletes_count desc
limit 1;
```

### Explanation of Alternate Solution:
- This alternative solution directly groups the data by the Olympics game and calculates the number of distinct athletes for each game.
- It then orders the result by the athlete count in descending order and limits the output to 1 row using `LIMIT 1`, giving us the Olympics with the highest number of athletes.

## Sample Data:
Assuming the following sample data for the `olympics_athletes_events` table:

| games      | name      |
|------------|-----------|
| 2020 Summer| Athlete1  |
| 2020 Summer| Athlete2  |
| 2020 Summer| Athlete3  |
| 2016 Summer| Athlete1  |
| 2016 Summer| Athlete4  |
| 2012 Summer| Athlete2  |
| ...        | ...       |

## Expected Output:
| games      | athletes_count |
|------------|----------------|
| 2020 Summer| 3              |

### Explanation of Expected Output:
- In the sample data, the Olympics game "2020 Summer" has the highest number of athletes, with a count of 3.
- Therefore, the expected output is the Olympics game "2020 Summer" along with the athlete count of 3.
