from django.contrib import admin
from core.models import DragonShelterProfile, AnimalResident, BookAnEncounterRequest, DragonShelterEvent

# Register your models here.
admin.site.site_header = 'Dragon Shelter Admin'
admin.site.site_title = 'Dragon Shelter Admin Panel'
admin.site.index_title = 'Welcome to Dragon Shelter Admin'

class BookAnEncounterRequestFilter(admin.ModelAdmin): 
    search_fields = ('name',)


class AnimalResidentFilter(admin.ModelAdmin): 
    search_fields = ('name',)
    list_filter = ('event_suitability','species','age')

admin.site.register(DragonShelterProfile)
admin.site.register(AnimalResident, AnimalResidentFilter)
admin.site.register(BookAnEncounterRequest, BookAnEncounterRequestFilter)
admin.site.register(DragonShelterEvent)