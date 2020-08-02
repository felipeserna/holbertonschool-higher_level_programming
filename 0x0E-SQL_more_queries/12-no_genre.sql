--  lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and
-- tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT t_s.title, t_s_g.genre_id
FROM tv_shows AS t_s
LEFT JOIN tv_show_genres AS t_s_g
ON t_s.id = t_s_g.show_id
WHERE t_s_g.show_id IS NULL
GROUP BY t_s.title ASC, t_s_g.genre_id ASC;
