from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models import Avg
from django.conf import settings

# Create your models here.
class Aktor(models.Model):
    imię = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    slug = models.SlugField(null=False)
    def __str__(self):
        return self.nazwisko+ " " +self.imię
    def get_absolute_url(self):
        return reverse("aktor_detail", kwargs={"slug": self.slug})  

class Rezyser(models.Model):
    imię = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    slug = models.SlugField(null=False)
    def __str__(self):
        return self.nazwisko+ " " +self.imię
    def get_absolute_url(self):
        return reverse("rezyser_detail", kwargs={"slug": self.slug})  

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=30)
    opis = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa
        
class Film(models.Model):
    nazwa = models.CharField(max_length=80)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    opis = models.CharField(max_length=250)
    aktorzy = models.ManyToManyField(Aktor, related_name='aktorzy')
    rezyser = models.ManyToManyField(Rezyser, related_name='rezyser')
    # srednia = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
    # ocena = models.ManyToManyField(Ocena)
    rok_produkcji = models.IntegerField()
    # ilosc_ocen = models.IntegerField()
    created = models.DateTimeField(
            default=timezone.now)
    updated = models.DateTimeField(
            default=timezone.now)
    slug = models.SlugField(null=False)
    
    # def publish(self):
        # self.updated = timezone.now()
        # self.save()
    def __str__(self):
        return self.nazwa
        
    def get_absolute_url(self):
        return reverse("film_detail", kwargs={"slug": self.slug})  
        
class Ocena(models.Model):
    ocena = (
        ('1', 'Okropny'),
        ('2', 'Słaby'),
        ('3', 'Średni'),
        ('4', 'Dobry'),
        ('5', 'Znakomity'),
    )
    wartość = models.IntegerField(choices=ocena,default=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.CharField(max_length=30)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, blank=False, null=False, related_name='oceny')
    published_date = models.DateTimeField(blank=True, null=True)

    def __int__(self):
        return self.wartość   
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()