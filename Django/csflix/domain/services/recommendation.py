from domain.models import Video
from video.models import Video as StoreVideo

# TDD
class RecommendationService:
    def __init__(self, video_model):
        self._video_model = video_model

    def get_recommendations_for_user(self, user):
        # "-" in order_by represents descending order
        store_videos = self._video_model.objects.filter(tags__name__in = user.interests).order_by("-created_at")[:10]

        return [ 
            Video.from_store_model(video=v, tags=v.tags.all())
            for v in store_videos
        ]

def get_recommendation_service():
    return RecommendationService(
        video_model=StoreVideo
    )
