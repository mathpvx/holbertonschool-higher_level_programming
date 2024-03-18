-- lists all records of the second_table in desc order and if name has a value
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;