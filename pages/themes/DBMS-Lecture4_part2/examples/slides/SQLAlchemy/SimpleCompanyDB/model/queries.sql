-- SELECT all employees who works for Google:
SELECT e.employee_id, e.employee_name
FROM   employee e
JOIN   company_employee ce ON e.employee_id = ce.employee_id
WHERE  ce.company_id = (SELECT company_id from company WHERE company_name LIKE 'Google');