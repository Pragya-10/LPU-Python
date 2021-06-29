class User:
    def __init__(self, id, name, email, interests, last_viewed):
        self.id = id
        self.name = name
        self.email = email
        self.interests = interests
        self.last_viewed = last_viewed

class Video:
    def __init__(self, id, title, genre, cast, video_file, tags, trending):
        self.id = id
        self.title = title
        self.genre = genre
        self.cast = cast
        self.video_file = video_file
        self.tags = tags
        self.trending = trending


    @classmethod
    def from_store_model(cls, video, tags):
        return cls(
            id=video.id,
            title=video.title,
            genre="",
            cast="",
            video_file=video.video_file.url,
            tags=tags,
            trending=True
        )
