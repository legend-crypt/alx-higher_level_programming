-- list all the cities of california
-- the name of the database will be passed as an argument

SELECT id, name
  FROM cities
 WHERE state_id = 1
ORDER BY cities.id ASC;
