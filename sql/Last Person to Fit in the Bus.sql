SELECT q1.person_name
FROM Queue q1
WHERE (
  SELECT SUM(q2.weight)
  FROM Queue q2
  WHERE q2.turn <= q1.turn
) <= 1000
ORDER BY q1.turn DESC
LIMIT 1


SELECT sub.person_name
FROM
(
  SELECT q.person_name,
         @running := @running + q.weight AS cum_weight,
         q.turn
  FROM Queue q
  CROSS JOIN (SELECT @running := 0) init
  ORDER BY q.turn
) sub
WHERE sub.cum_weight <= 1000
ORDER BY sub.turn DESC
LIMIT 1
