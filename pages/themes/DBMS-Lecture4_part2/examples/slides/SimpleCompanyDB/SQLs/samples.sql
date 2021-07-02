-- select from many-to-many with INNER JOIN
SELECT
    employee.employee_id,
    company.company_id,
    employee.employee_name,
    company.company_name,
FROM employee
INNER JOIN company_employee ON employee.employee_id = company_employee.employee_id
INNER JOIN company ON company.company_id = company_employee.company_id

-- select all employees working for google:
SELECT
    employee.employee_id,
    company.company_id,
    employee.employee_name,
    company.company_name,
FROM company
INNER JOIN company_employee ON employee.employee_id = company_employee.employee_id
INNER JOIN employee ON company.company_id = company_employee.company_id