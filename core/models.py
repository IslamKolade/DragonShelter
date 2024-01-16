from django.db import models
import cloudinary
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
          
          
# Create your models here.

class DragonShelterProfile(models.Model):
    facebook_url = models.URLField(max_length=10000, null=True, blank=True)
    instagram_username = models.CharField(max_length=10000, null=True, blank=True)
    twitter_username = models.CharField(max_length=10000, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=10000, null=True, blank=True)
    booking_enquiries_email = models.CharField(max_length=10000, null=True, blank=True)
    phone_number = models.CharField(max_length=10000, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=10000, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Dragon Shelter Profile'
    
class AnimalResident(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    slug = models.SlugField(max_length=10000, blank=True, editable=False)
    age = models.CharField(max_length=10000, null=True, blank=True)
    species = models.CharField(max_length=10000, null=True, blank=True)
    story = models.TextField(null=True, blank=True)
    CHOICES = (
        ('All ages', 'All ages'),
        ('7+ ages', '7+ ages'),
        ('Not suitable', 'Not suitable'),
    )
    event_suitability = models.CharField(
        max_length=10000,
        choices=CHOICES,
        default='All ages',
        null=True, blank=True,
    )
    animal_picture = CloudinaryField('animal picture')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AnimalResident, self).save(*args, **kwargs)

    def __str__(self):
        return f"Reptile Profile: {self.name}"

class BookAnEncounterRequest(models.Model):
    name = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    phone_number = models.CharField(max_length=10000)
    event_description = models.TextField()
    preferred_date_of_event = models.CharField(max_length=10000)

    def __str__(self):
        return f"Encounter Request By: {self.name} for {self.preferred_date_of_event}"
    
class DragonShelterEvent(models.Model):
    event_date = models.DateField()

    def __str__(self):
        return f'Event Date: {self.event_date}'



class PaddyPony(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    age = models.CharField(max_length=10000, null=True, blank=True)
    species = models.CharField(max_length=10000, null=True, blank=True)
    story = models.TextField(null=True, blank=True)
    CHOICES = (
        ('All ages', 'All ages'),
        ('7+ ages', '7+ ages'),
        ('Not suitable', 'Not suitable'),
    )
    event_suitability = models.CharField(
        max_length=10000,
        choices=CHOICES,
        default='All ages',
        null=True, blank=True,
    )
    pony_profile_picture = CloudinaryField('pony profile picture')
    photo_1 = CloudinaryField('photo 1', blank=True, null=True,)
    photo_2 = CloudinaryField('photo 2', blank=True, null=True,)
    photo_3 = CloudinaryField('photo 3', blank=True, null=True,)
    photo_4 = CloudinaryField('photo 4', blank=True, null=True,)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PaddyPony, self).save(*args, **kwargs)

    def __str__(self):
        return f"Pony Profile: {self.name}"

