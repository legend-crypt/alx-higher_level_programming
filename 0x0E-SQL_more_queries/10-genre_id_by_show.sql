-- list the tv show and generes of movies
-- the result show be sorted by tv_shows.titlle
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows, tv_show_genres
 WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
