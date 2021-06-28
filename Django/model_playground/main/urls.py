from django.urls import path

from main.views import HomeView, PizzaDetailView, MyPizzaDetailView

urlpatterns = [
    path("", HomeView.as_view()),
    path("pizzas/<int:pk>", MyPizzaDetailView.as_view())
]
