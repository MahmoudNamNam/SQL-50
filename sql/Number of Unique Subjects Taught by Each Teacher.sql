SELECt teacher_id ,count(Distinct subject_id) as cnt 
from Teacher 
group by teacher_id