# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
  
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Aktor, Rezyser, Film, Ocena, Kategoria
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm


class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"

class FilmDetailView(DetailView):
    model = Film
    template_name = "film_detail.html"

class AktorListView(ListView):
    model = Aktor
    template_name = "aktor_list.html"

class AktorDetailView(DetailView):
    model = Aktor
    template_name = "aktor_detail.html"

class RezyserListView(ListView):
    model = Rezyser
    template_name = "rezyser_list.html"

class RezyserDetailView(DetailView):
    model = Rezyser
    template_name = "rezyser_detail.html"

def ocena_list(request):
    ocena = Ocena.objects.filter(user=request.user).order_by('film')
    return render(request, 'ocena_list.html', {'ocena': ocena})

def ocena_details(request, pk):
    ocena = get_object_or_404(Ocena, pk=pk)
    return render(request, 'ocena_details.html', {'ocena': ocena})    

def ocena_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            ocena = form.save(commit=False)
            ocena.user = request.user
            ocena.published_date = timezone.now()
            ocena.save()
            return redirect('ocena_details', pk=ocena.pk)
    else:
        form = PostForm()
    return render(request, 'ocena_new.html', {'form': form})
    
def ocena_edit(request, pk):
    ocena = get_object_or_404(Ocena, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=ocena)
        if form.is_valid():
            ocena = form.save(commit=False)
            ocena.user = request.user
            ocena.published_date = timezone.now()
            ocena.save()
            return redirect('ocena_details', pk=ocena.pk)
    else:
        form = PostForm(instance=ocena)
    return render(request, 'ocena_edit.html', {'form': form})

def index(request):
    filmy = Film.objects.order_by('nazwa')[:5]
    context = {'filmy': filmy}
    return render(request, 'index.html', context)

# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    
# def index(request):
   # aktorzy = Aktor.objects.order_by('nazwisko')[:5]
   # template = loader.get_template('Film_/index.html')
   # context = {
       # 'aktorzy': aktorzy,
   # }
   # return HttpResponse(template.render(context, request))
    #output = ', '.join([q.nazwisko+" "+q.imię for q in aktorzy])
    #return HttpResponse(output)
