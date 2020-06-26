from django.db import models
from django.urls import reverse
# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Fish(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0],
    )

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"Time for {self.get_meal_display}!!"

