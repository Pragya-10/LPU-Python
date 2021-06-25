class User:
    def __init__(self, id, name, email, interests, last_viewed):
        self.id = id
        self.name = name
        self.email = email
        self.interests = interests
        self.last_viewed = last_viewed

class Video:
    def __init__(self, title, genre, cast, tags, trending):
        self.title = title
        self.genre = genre
        self.cast = cast
        self.tags = tags
        self.trending = trending
