from datetime import datetime
from domain.models import Video
from video.models import Video as VideoStore
from main.models import History as HistoryStore


class VideoService:
    def __init__(self, video_model, history_model):
        self._video_model = video_model
        self._history_model = history_model

    def get_video_for_user(self, user, video_id):
        video = self._video_model.objects.get(pk = video_id)

        obj, created = self._history_model.objects.update_or_create(
            user_id=user.id, video_id=video_id,
            defaults={
                "user_id": user.id, 
                "video_id": video_id, 
                "last_seen": datetime.now(),
            },
        )

        return Video.from_store_model(video=video, tags=video.tags.all())

def get_video_service():
    return VideoService(
        video_model=VideoStore,
        history_model=HistoryStore
    )
