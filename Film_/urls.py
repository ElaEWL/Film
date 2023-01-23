"""Film URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views
from .views import FilmListView, FilmDetailView, AktorDetailView, AktorListView, RezyserDetailView, RezyserListView

urlpatterns = [
    
    path("", views.index, name='index'),
    path("Filmy/<slug:slug>", FilmDetailView.as_view(), name="film_detail"),
    path("Filmy", FilmListView.as_view(), name="film_list"),
    path("Aktorzy/<slug:slug>", AktorDetailView.as_view(), name="aktor_detail"),
    path("Aktorzy", AktorListView.as_view(), name="aktor_list"),
    path("Rezyserzy/<slug:slug>", RezyserDetailView.as_view(), name="rezyser_detail"),
    path("Rezyserzy", RezyserListView.as_view(), name="rezyser_list"),
    path("Ocena/", views.ocena_list, name='ocena_list'),
    path("Ocena/<int:pk>/", views.ocena_details, name='ocena_details'),
    path("Ocena/new/", views.ocena_new, name='ocena_new'),
    path('Ocena/<int:pk>/edit/', views.ocena_edit, name='ocena_edit'),
]


