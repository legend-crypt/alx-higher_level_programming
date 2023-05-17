-- a script that list all records of the table second_table
-- the name of the database will be passed as an argument 
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
