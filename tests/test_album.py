from lib.album import Album

"""
When I construct an Album
With the fields id, title, 
release_year, and artist_id
They are reflected in the instance properties
"""
def test_constucts_with_fields():
    album = Album(1, "Ascension", 1966, 1)
    assert album.id == 1
    assert album.title == "Ascension"
    assert album.release_year == 1966
    assert album.artist_id == 1

"""
When I construct two Albums with the same
fields they are equal

***(Make sure the attributes eg. "id" included 
->objects in the class are represented and not 
just the table categorization format from 
the seed/input.)
"""
def test_equality():
    artist_1 = Album(1, "Doolittle", 1989, 1)
    artist_2 = Album(1, "Doolittle", 1989, 1)
    assert artist_1 == artist_2

"""
When I construct an Artist 
and I format it to a string
then it comes out in a format
that looks nicer.
"""
album = Album(1, "Doolittle", 1989, 1)
assert str(album) == "Album(1, Doolittle, 1989, 1)"