select name, bonus.bonus as bonus from employee
left join bonus
on employee.empid = bonus.empid
having bonus < 1000 or bonus is null;
