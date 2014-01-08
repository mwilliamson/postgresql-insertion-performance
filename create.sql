CREATE TABLE album (
    id serial PRIMARY KEY,
    title varchar(40) NOT NULL,
    year integer NOT NULL
);

CREATE TABLE song (
    id serial PRIMARY KEY,
    album_id integer NOT NULL REFERENCES album(id),
    name varchar(40) NOT NULL
);
