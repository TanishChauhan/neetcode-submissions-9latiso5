-- Write your query below


select c.customer_id,c.name
from customers c
join orders o
on
o.customer_id=c.customer_id
join product p
on 
p.product_id=o.product_id
group by c.name,c.customer_id

having 
sum( 
    case when order_date between '2020-06-01' and '2020-06-30'
    then (o.quantity * p.price)
    else 0
    end
) >= 100
and
sum( 
    case when order_date between '2020-07-01' and '2020-07-31'
    then (o.quantity * p.price)
    else 0
    end
) >= 100