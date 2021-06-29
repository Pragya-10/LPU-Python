from django.urls import path
from video.views import VideoConsumptionView

urlpatterns = [
    path("<int:pk>/", VideoConsumptionView.as_view())
]
