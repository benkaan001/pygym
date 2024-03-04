# Question:

Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. If a customer had more than one order on a certain day, sum the order costs on a daily basis. Output the customer's first name, total cost of their items, and the date.

For simplicity, you can assume that every first name in the dataset is unique.

## Solution:

```sql
select
    first_name,
    order_date,
    total_cost
from customers
join
    (select
        sum(total_order_cost) as total_cost,
        cust_id,
        order_date,
        row_number() over (order by sum(total_order_cost) desc) as rnk
    from orders
    where order_date between '2019-02-01' and '2019-05-01'
    group by cust_id, order_date) t
on t.cust_id = customers.id
where rnk = 1;
```

### Explanation of Solution:
- This query selects the customer's first name (`first_name`), the order date (`order_date`), and the total cost of their items (`total_cost`).
- The inner query calculates the daily total order cost for each customer between the specified date range.
- The `row_number() over (order by sum(total_order_cost) desc)` function assigns a rank to each row based on the sum of the total order cost, in descending order.
- The outer query joins the results with the `customers` table and selects the row with rank 1, representing the customer with the highest daily total order cost.

## Alternate Solution:

```sql
select
    c.first_name,
    o.order_date,
    sum(o.total_order_cost) as total_cost
from customers c
join orders o
on c.id = o.cust_id
where order_date between '2019-02-01' and '2019-05-01'
group by o.cust_id, o.order_date
order by total_cost desc
limit 1;
```

### Explanation of Alternate Solution:
- This alternative solution directly joins the `customers` and `orders` tables, grouping the data by customer ID and order date.
- It calculates the sum of the total order cost for each customer on each order date.
- The result is then ordered by total cost in descending order, and `LIMIT 1` is used to retrieve only the customer with the highest daily total order cost.

## Sample Data:
Assuming the following sample data for the `customers` and `orders` tables:

**Customers Table:**

| id | first_name |
|----|------------|
| 1  | John       |
| 2  | Alice      |
| 3  | Bob        |

**Orders Table:**

| order_id | cust_id | order_date | total_order_cost |
|----------|---------|------------|------------------|
| 101      | 1       | 2019-02-01 | 50               |
| 102      | 2       | 2019-02-01 | 70               |
| 103      | 1       | 2019-02-02 | 30               |
| ...      | ...     | ...        | ...              |

## Expected Output:
| first_name | order_date | total_cost |
|------------|------------|------------|
| John       | 2019-02-01 | 80         |

### Explanation of Expected Output:
- In the sample data, John has two orders on 2019-02-01 with total costs of 50 and 30, summing up to 80.
- This is the highest daily total order cost, so John's information on that date is the expected output.