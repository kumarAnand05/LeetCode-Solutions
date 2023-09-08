select employeeuni.unique_id, name from employees
left join employeeuni
on employees.id = employeeuni.id
