-- script to list all comedy show in the database
-- the name of the database will be passed in the command argument
SELECT tv_shows.title
  FROM tv_shows
 JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
 JOIN tv_genres
  ON tv_genres.id = tv_show_genres.genre_id
  AND tv_genres.name = "Comedy"
 ORDER BY tv_shows.title ASC;
