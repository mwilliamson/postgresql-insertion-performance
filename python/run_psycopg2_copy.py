#/usr/bin/env python

import io

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
    
    fileobj = io.StringIO()
    for song_index in range(10000):
        fileobj.write(u"{0}\tSong {1}\n".format(album_id, song_index))
    fileobj.seek(0)
    
    cursor.copy_from(
        file=fileobj,
        table="songs",
        columns=["album_id", "title"],
    )


if __name__ == "__main__":
    main()
