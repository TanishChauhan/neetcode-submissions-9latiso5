-- Write your query below

select name from sales_person
where sales_id NOT in
(
    select sales_id from orders o
    join company c
    on
    o.com_id=c.com_id
    where name = 'CRIMSON'
    
)