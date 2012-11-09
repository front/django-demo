from django.forms import ModelForm
from app.models import Goal, Action

class GoalForm(ModelForm):
  class Meta:
      model = Goal

class ActionForm(ModelForm):
  class Meta:
      model = Action
