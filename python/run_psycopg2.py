#/usr/bin/env python

import psycopg2


def main():
    with psycopg2.connect("dbname=insert_perf") as connection:
        cursor = connection.cursor()
        for album_index in range(0, 10):
            album_id = _create_album(cursor, album_index)
            _create_songs(cursor, album_id)
            
        connection.commit()


def _create_album(cursor, album_index):
    cursor.execute(
        "INSERT INTO albums (title, year) VALUES (%s, %s) RETURNING id",
        ("Album {0}".format(album_index), "2014",)
    )
    return cursor.fetchone()[0]


def _create_songs(cursor, album_id):
    assert album_id is not None
    
    songs = [
        (album_id, "Song {0}".format(song_index))
        for song_index in range(0, 10000)
    ]
    
    cursor.executemany(
        "INSERT INTO songs (album_id, title) VALUES (%s, %s)",
        songs
    )


if __name__ == "__main__":
    main()
