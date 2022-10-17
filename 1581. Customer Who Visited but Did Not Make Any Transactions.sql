# Write your MySQL query statement below
select t1.customer_id, count(t1.visit_id) as count_no_trans 
from visits t1
where visit_id not in (select visit_id from transactions ) 
group by customer_id
order by customer_id
