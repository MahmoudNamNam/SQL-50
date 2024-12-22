-- Select employee_id and department_id from Employee table
SELECT employee_id, 
       department_id
FROM Employee
-- Filter rows where primary_flag is 'Y'
WHERE primary_flag = 'Y'
   -- Or select employees who do not have any primary department
   OR employee_id NOT IN (SELECT employee_id FROM Employee WHERE primary_flag = 'Y');
