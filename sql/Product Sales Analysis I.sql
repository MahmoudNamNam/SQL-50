select product_name ,year,price
from Sales s
inner join Product p
on s.product_id  = p.product_id  