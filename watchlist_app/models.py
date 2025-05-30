from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey('StreamPlatform', on_delete=models.CASCADE, related_name='watchlist')

    def __str__(self):
        return self.title


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=200)


    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey('WatchList', on_delete=models.CASCADE, related_name='reviews')
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.watchlist.title} | {self.description}"
