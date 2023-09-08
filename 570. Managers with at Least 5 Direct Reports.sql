select name from employee
where id in (select managerId from employee
group by managerID
having count(managerid)>=5)
