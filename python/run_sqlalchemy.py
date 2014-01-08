#/usr/bin/env python

import sqlalchemy.orm
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable=False)
    year = Column(Integer, nullable=False)


class Song(Base):
    __tablename__ = "songs"
    
    id = Column(Integer, primary_key=True)
    album_id = Column(Integer, ForeignKey(Album.id))
    album = relationship(Album)
    title = Column(String(40), nullable=False)
    

def main():
    engine = sqlalchemy.create_engine("postgresql:///insert_perf")
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    try:
        for album_index in range(0, 10):
            album = _create_album(session, album_index)
            _create_songs(session, album)
            
        session.commit()
    finally:
        session.close()


def _create_album(session, album_index):
    album = Album(
        title="Album {0}".format(album_index),
        year="2014",
    )
    session.add(album)
    session.flush()
    return album


def _create_songs(session, album):
    assert album.id is not None
    
    songs = [
        dict(album_id=album.id, title="Song {0}".format(song_index))
        for song_index in range(0, 10000)
    ]
    
    session.execute(
        Song.__table__.insert(),
        songs,
    )


if __name__ == "__main__":
    main()
