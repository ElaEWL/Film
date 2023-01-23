# from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views import View  
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Aktor, Rezyser, Film, Ocena, Kategoria
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    context = {}
    if request.user.is_authenticated:
        # Do something for authenticated users.
        context['userStatus'] = 'zalogowany'
    else:
        # Do something for anonymous users.
        context['userStatus'] = 'niezalogowany'
    return render(request, 'home.html', context)
    
def signup_page(request):
    context = {}
    if request.method == 'POST':
        # Request for sign up
        # Check if user is available
        try:
            user = User.objects.get(username=request.POST['username'])
            context['error'] = 'Podana nazwa użytkownika już istnieje! Proszę podać inną nazwę użytkownika.'
            return render(request, 'signup.html', context)
        except User.DoesNotExist:
            # Check if the password1 is equal to the password2
            if request.POST['password1'] != request.POST['password2']:
                context['error'] = 'Podane hasła nie są takie same! Proszę wprowadzić identyczne hasła.'
                return render(request, 'signup.html', context)
            else:
                # Create new user
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # Automatic login after signing up
                auth.login(request, user)
                # Go to home page
                return redirect('home')
    else:
        return render(request, 'signup.html', context)
        
def login_page(request):
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] ,password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.POST.get('redir'):
                return redirect(f"{request.POST.get('redir')}")
            else:
                return redirect('home')
        else:
            context['error'] = 'Podane hasło lub login są błędne! Podaj poprawne dane.'
            if request.POST.get('redir'):
                context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
                context['nextURL'] = request.GET.get('next')
            return render(request, 'login.html', context)
    else:
        if request.GET.get('next'):
            context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
            context['nextURL'] = request.GET.get('next')
        return render(request, 'login.html', context)
            
def logout_page(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
        
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

@login_required  
def ocena_list(request):
    ocena = Ocena.objects.filter(user=request.user).order_by('film')
    return render(request, 'ocena_list.html', {'ocena': ocena})

@login_required 
def ocena_details(request, pk):
    ocena = get_object_or_404(Ocena, pk=pk)
    return render(request, 'ocena_details.html', {'ocena': ocena})    

@login_required 
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

@login_required   
@permission_required('Filmy_.can_edit', raise_exception=True)  
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
