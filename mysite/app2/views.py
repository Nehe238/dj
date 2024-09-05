from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'app2/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)