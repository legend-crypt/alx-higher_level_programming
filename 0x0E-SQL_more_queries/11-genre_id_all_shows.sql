-- script to the display all tv_show.title and tv_show_genres.genre_id
-- the name of the database will be provided in the in command 
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
