select user_id, max(time_stamp) as last_stamp
from logins
where
 EXTRACT(YEAR FROM time_stamp::timestamp) = 2020
group by user_id