-- script lists all shows that don't have a genre linked to them and orders them by title and genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.genre_id IS NULL
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;