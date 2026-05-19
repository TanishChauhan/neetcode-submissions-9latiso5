-- Write your query below

select left_operand,operator,right_operand,
case when operator ='>' then v1.value > v2.value 
 when operator ='<' then v1.value < v2.value 
 when operator ='=' then v1.value = v2.value 
end as value  
from expressions e
join variables v1 on v1.name=e.left_operand
join variables v2 on v2.name=e.right_operand 
