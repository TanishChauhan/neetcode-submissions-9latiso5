-- Write your query below

select name from sales_person sp
where NOT EXISTS
(
    select 1 from company c
    join
    orders o
    on
    o.com_id=c.com_id
    where c.name='CRIMSON'
    and
    o.sales_id=sp.sales_id
)