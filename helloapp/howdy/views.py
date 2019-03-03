from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# howdy/views.py
from django.views.generic import TemplateView
from .models import Choice

# Create your views here.
# class HomePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)

def index(request):
    users = Choice.objects.all()
    context = {
        # 'name': users.name, 
    'users': users
    }
    return render(request, 'index.html', context=context)


