from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from domain.services.user import get_user_service
from domain.services.video import get_video_service

# Create your views here.
class VideoConsumptionView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = "video/video-consumption.html"
    
    def get(self, request, pk):
        user = get_user_service().get_user_by_id(request.user.id)
        video = get_video_service().get_video_for_user(user=user, video_id=pk)

        context = {
            "video": video
        }

        return self.render_to_response(context)
