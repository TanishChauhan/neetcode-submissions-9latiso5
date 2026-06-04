-- Write your query below

select c.title
from content c
join
tv_program t
on c.content_id=t.content_id
where kids_content ='Y'
and content_type = 'Movies'
and program_date between '2020-06-01 00:00' and '2020-06-30 23:59'
group by c.title