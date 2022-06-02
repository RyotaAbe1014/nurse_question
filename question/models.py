from django.db import models

# Create your models here.
class Question(models.Model):
  title = models.CharField(max_length=255)
  option1 = models.CharField(max_length=255)
  option2 = models.CharField(max_length=255)
  option3 = models.CharField(max_length=255)
  option4 = models.CharField(max_length=255)
  answer = models.IntegerField()