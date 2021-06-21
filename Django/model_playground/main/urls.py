from django.urls import path

from main.views import HomeView, PizzaDetailView

urlpatterns = [
    path("", HomeView.as_view()),
    path("pizzas/<int:pk>", PizzaDetailView.as_view())
]
