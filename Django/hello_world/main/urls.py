from django.urls import path

from main.views import HelloWorldView, TablePageView

urlpatterns = [
    path('hello/', HelloWorldView.as_view()),
    path('tables/', TablePageView.as_view())
]
