from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()