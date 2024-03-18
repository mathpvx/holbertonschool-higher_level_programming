-- lists all records of the table second_table
-- selects records in the order wanted
SELECT `score`, `name`
-- pick the choosen table
FROM `second_table`
-- condition
WHERE `score`>= 10
-- in descending order
ORDER BY `score` DESC;