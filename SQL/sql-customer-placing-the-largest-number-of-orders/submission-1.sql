-- Write your query below
select
customer_number from 
(
    select customer_number,
    RANK() over ( order by count(*) desc)
    as rn
    from orders
    group by customer_number
)t
where rn=1