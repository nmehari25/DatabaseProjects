from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository



# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List (artists) them out
for artist in artists:
    print(artist)

# Retreive all albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

# List (albums) them out
for album in albums:
    print(album)