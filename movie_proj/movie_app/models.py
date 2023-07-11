from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Director(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    director_email = models.EmailField()

    def get_url(self):
        return reverse('direct_info', args=[self.id])

    def __str__(self):
        return f'{self.id}) {self.first_name} {self.last_name}'


class Actor(models.Model):

    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)

    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def get_url(self):
        return reverse('actor_info', args=[self.id])

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер - {self.first_name} {self.last_name}'
        else:
            return f'Актриса - {self.first_name} {self.last_name}'


class Movie(models.Model):

    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    years = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_info', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
