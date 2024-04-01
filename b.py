import random

class User:
    def __init__(self, name):
        self.name = name
class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class Playlist:

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        total_rating = sum(rating.value for rating in self.ratings)
        return total_rating / len(self.ratings)
class Rating:
    def __init__(self, value):
        self.value = value
# Create users
user1 = User("User1")
user2 = User("User2")
user3 = User("User3")

# Randomly generate ratings for playlists and audios
def generate_random_rating():
    return random.randint(1, 5)

# Create playlists and audios
playlist1 = Playlist("Playlist1", "Genre1")
playlist2 = Playlist("Playlist2", "Genre2")

audio1 = Audio("Audio1", "url1")
audio2 = Audio("Audio2", "url2")

# Add audios to playlists
playlist1.add_audio(audio1)
playlist1.add_audio(audio2)

# Add random ratings to playlists
playlist1.add_rating(Rating(generate_random_rating()))
playlist1.add_rating(Rating(generate_random_rating()))
playlist2.add_rating(Rating(generate_random_rating()))

# Display average rating
print(f"Average rating for {playlist1.name}: {playlist1.get_average_rating()}")
print(f"Average rating for {playlist2.name}: {playlist2.get_average_rating()}")