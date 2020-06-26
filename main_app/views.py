from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fish_index(request):
    fish = Fish.objects.all()
    return render(request, 'fish/index.html', { 'fish': fish })

def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fish/details.html', { 'fish': fish })

class FishList(ListView):
    model = Fish
    template_name = 'about.html'

class FishCreate(CreateView):
    model = Fish
    fields = '__all__'

class FishUpdate(UpdateView):
    model = Fish
    fields = ['breed', 'color', 'description']

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fish/index/'