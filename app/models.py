from django.db import models

from django.contrib.admin.models import User

class Strategy(models.Model):
  title = models.CharField(max_length=250)
  vision = models.CharField(max_length=250)
  user = models.ForeignKey(User)

  def __str__(self):
    return self.title;

class Goal(models.Model):
  title = models.CharField(max_length=250)
  strategy = models.ForeignKey('Strategy')

  def __str__(self):
    return self.title;

class Action(models.Model):
  challenge = models.CharField(max_length=250)
  start_date = models.DateTimeField()
  goal = models.ForeignKey('Goal')

  def __str__(self):
    return self.challenge;
