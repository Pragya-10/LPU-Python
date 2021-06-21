from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render

from main.models import Pizza

# Create your views here.
# class HomeView(TemplateView):
#     template_name = "main/index.html"

#     def get_context_data(self, **kwargs):
#         search = self.request.GET.get("search", "")

#         pizzas = Pizza.objects.filter(name__icontains = search)

#         return {
#             "pizzas": pizzas
#         }

class HomeView(ListView):
    template_name = "main/index.html"
    context_object_name = "pizzas"

    def get_queryset(self):
        search = self.request.GET.get("search", "")

        return Pizza.objects.filter(name__icontains = search)


class PizzaDetailView(DetailView):
    queryset = Pizza.objects.all()
    template_name = "main/pizza.html"
    context_object_name = "pizza"

# def handle_get_pizza(request, pk):
#     pizza = Pizza.objects.get(pk = pk)

#     context = {
#         "pizza": pizza
#     }

#     return render(request, "main/pizza.html", context)
