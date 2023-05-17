-- script to list the number of records with the same in second_table
-- the name of the databse will be passed as an arguement to the mysql command
SELECT score, COUNT(score) AS number  FROM second_table
GROUP BY score
ORDER BY score DESC; 
