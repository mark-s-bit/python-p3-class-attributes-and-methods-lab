class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment song count
        Song.add_song_to_count()
        
        # Add artist and genre
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        
        # Update artist and genre counts
        Song.add_to_artist_count(artist)
        Song.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Testing the implementation
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
god_plan = Song("God's Plan", "Drake", "Rap")
crazy_love = Song("Crazy in Love", "Beyonce", "Pop")

# Check song count
print(Song.count)  # 4

# Check unique artists
print(Song.artists)  # ['Jay-Z', 'Beyonce', 'Drake']

# Check unique genres
print(Song.genres)  # ['Rap', 'Pop']

# Check genre count
print(Song.genre_count)  # {'Rap': 2, 'Pop': 2}

# Check artist count
print(Song.artist_count)  # {'Jay-Z': 1, 'Beyonce': 2, 'Drake': 1}
