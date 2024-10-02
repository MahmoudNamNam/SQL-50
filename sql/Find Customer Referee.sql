SELECT name
FROM Customer
WHERE COALESCE(referee_id,0) != 2;




--- or


SELECT  name
FROM    Customer
WHERE  NOT referee_id = 2 OR referee_id IS NULL;