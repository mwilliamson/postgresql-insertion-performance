CREATE TABLE albums (
    id serial PRIMARY KEY,
    title varchar(40) NOT NULL,
    year integer NOT NULL
);

CREATE TABLE songs (
    id serial PRIMARY KEY,
    album_id integer NOT NULL REFERENCES albums(id),
    title varchar(40) NOT NULL
);
