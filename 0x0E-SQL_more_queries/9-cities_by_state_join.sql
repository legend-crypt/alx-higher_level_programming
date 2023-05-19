-- script to list all cities contained in the database
-- the name of the database will passed in the command argument
SELECT cities.id, cities.name, states.name
  FROM cities, states
 WHERE cities.state_id = states.id
 ORDER BY cities.id ASC;
