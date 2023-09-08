select project_id, round(avg(experience_years),2) as average_years 
from (select project_id, Project.employee_id, employee.experience_years from Project
left join employee
on employee.employee_id=project.employee_id) as t
group by project_id
order by project_id
