from lib.album import Album
class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    # This method executes an SQL query on the database.
    # It allows you to set some parameters too.
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        # albums = []
        # for row in rows:
        #     album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        #     albums.append(album)
        # return albums
        """ 
        Alternative refactored way to write
        the code above
        ***List comprehension example***
        """
        return [Album(row["id"], 
            row["title"], 
            row["release_year"], 
            row["artist_id"])
            for row in rows
        ]

