-- this script lists all shows and genres linked to that show from the database

SELECT tv_shows.title, tv_genres.name FROM tv_shows, tv_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_show_genres ON tv_show_genres.genre_id = tv.genres.id
    ORDER BY tv_shows.title ASC, tv_genres.name ASC;