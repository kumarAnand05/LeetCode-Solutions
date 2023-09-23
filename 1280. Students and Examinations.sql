select t1.student_id, t1.student_name, t1.subject_name, count(e.subject_name) as attended_exams 
from (select * from students
cross join subjects) as t1
left join examinations as e
on t1.student_id = e.student_id
and t1.subject_name = e.subject_name
group by student_id,subject_name
order by student_id, subject_name
