from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

class HomeView(TemplateView):
    template_name = 'app1/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ApplicationView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')
