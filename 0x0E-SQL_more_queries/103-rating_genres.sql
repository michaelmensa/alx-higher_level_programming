-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- lists all rows of a table by the sum of a linked row

SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre.id
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
