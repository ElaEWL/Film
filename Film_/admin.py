from django.contrib import admin
from .models import Aktor, Rezyser, Film, Ocena, Kategoria
# Register your models here.

class AktorAdmin(admin.ModelAdmin):
    fields = ['imię','nazwisko','slug']
    list_display = ('id','imię', 'nazwisko')
    list_display_links = ['id','nazwisko']
    search_fields = ['nazwisko']
    prepopulated_fields = {"slug": ("nazwisko",)}
admin.site.register(Aktor, AktorAdmin)

class RezyserAdmin(admin.ModelAdmin):
    fields = ['imię','nazwisko','slug']
    list_display = ('id','imię', 'nazwisko')
    list_display_links = ['id','nazwisko']
    search_fields = ['nazwisko']
    prepopulated_fields = {"slug": ("nazwisko",)}
admin.site.register(Rezyser, RezyserAdmin)

class FilmAdmin(admin.ModelAdmin):
    fields = ['nazwa','slug','kategoria','opis','aktorzy','rezyser','rok_produkcji','created','updated']
    list_display = ['id','nazwa', 'kategoria','opis','rok_produkcji']
    list_display_links = ['id','nazwa']
    search_fields = ['nazwa']
    prepopulated_fields = {"slug": ("nazwa",)}
admin.site.register(Film, FilmAdmin)

class OcenaAdmin(admin.ModelAdmin):
    fields = ['wartość', 'user','film','published_date']
    list_display = ('id','wartość', 'user','film','published_date')
    list_display_links = ['id']
admin.site.register(Ocena, OcenaAdmin)

class KategoriaAdmin(admin.ModelAdmin):
    fields = ['nazwa','opis']
    list_display = ('id','nazwa','opis')
    list_display_links = ['id','nazwa']
admin.site.register(Kategoria, KategoriaAdmin)

class MembershipInline(admin.TabularInline):
    model = Film.aktorzy.through

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ['aktorzy']