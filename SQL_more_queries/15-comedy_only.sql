-- the script outputs a list of all comedy shows in the database

SELECT tv_shows.title
    FROM tv_shows JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_genres.name = "Comedy"
    ORDER BY tv_shows.title ASC;