from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=25)
    title=models.CharField(max_length=50)
    description=models.TextField()
    due=models.DateTimeField()
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    data=models.CharField(max_length=150)
    status=models.BooleanField(default=False)