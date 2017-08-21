import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    polls_heading = models.CharField(max_length=200)
  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.polls_heading
   


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    polls_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.polls_choice
