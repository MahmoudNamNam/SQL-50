select unique_id , name
from Employees e 
left join EmployeeUNI ue
on e.id = ue.id