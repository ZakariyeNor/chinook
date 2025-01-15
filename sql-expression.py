from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instroction from our localhost "chinook" db

db = create_engine("postgresql:///chinook")

meta = MetaData('db')

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)


# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Float),
    Column("Bytes", Integer),
    Column("Unitprice", Float)
)


# making the connection 
with db.connect() as connection:

    # Query 1 - Select all records from the "artist" table
    # select_query = artist_table.select()

    # Query 1 - Select only the "name" column from the artist table
    select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    results = connection.execute(select_query)
    for result in results:
        print(result)