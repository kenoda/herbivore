from django.db import models
from django.utils import timezone


# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     user_text = models.CharField(max_length=300)


class Plant(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=30)
    plant_text = models.TextField()


class Post(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="posts")
    created_date = models.DateTimeField(default=timezone.now)
    # pub_date = models.DateTimeField(blank=True, null=True)
    plant_height = models.IntegerField(default=0)
    description = models.TextField()
