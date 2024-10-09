select name , bonus
from Employee E LEFT OUTER JOIN
Bonus B on E.empId = B.empId
WHERE bonus < 1000 OR bonus IS NULL