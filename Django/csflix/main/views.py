from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from domain.services.user import get_user_service
from domain.services.recommendation import get_recommendation_service

# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'main/home.html'

    def get(self, request):
        user = get_user_service().get_user_by_id(request.user.id)
        videos = get_recommendation_service().get_recommendations_for_user(user)

        return self.render_to_response({
            "videos": videos
        })

