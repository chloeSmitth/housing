from django.db import models

# Create your models here.
class Amenitie(models.Model):
    amenity = models.CharField(max_length=200)
    def __str__(self):
        return self.amenity


class Housing(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    HOUSING_TYPES = [
        ("Apartment", "Apartment"),
        ("House","House"),
        ("Town_House","Town House"),
    ]
    housing_type = models.CharField(max_length = 10, choices=HOUSING_TYPES, blank = False)
    pub_date = models.DateTimeField('date published')
    amenities = models.ManyToManyField(Amenitie, blank=True)
    admin_check = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.ForeignKey('Housing', on_delete=models.CASCADE)
    people = models.IntegerField(blank = True)
    beds = models.IntegerField(blank = True)
    baths = models.IntegerField(blank = True)
    rent = models.IntegerField(blank=True)
    def __str__(self):
        return self.name.name
