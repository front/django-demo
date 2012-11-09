from django.shortcuts import render_to_response, redirect

from app.models import Strategy, Goal, Action
from app.forms import GoalForm, ActionForm

def index(request):
  strategy = Strategy.objects.get();
  goals = Goal.objects.filter(strategy_id=strategy.pk);

  for goal in goals:
    goal.actions = Action.objects.filter(goal_id=goal.pk)

  return render_to_response('index.html', {'strategy': strategy, 'goals': goals, 'form_goal': GoalForm, 'form_action': ActionForm});

def add_goal(request):
  if request.method == 'POST':
    form = GoalForm(request.POST)
    if form.is_valid():
      form.save()

  return redirect('index');

def add_action(request):
  if request.method == 'POST':
    form = ActionForm(request.POST)
    if form.is_valid():
      form.save()

  return redirect('index');

