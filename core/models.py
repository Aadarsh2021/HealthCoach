from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    dietary_habits = models.TextField(null=True, blank=True)
    exercise_routines = models.TextField(null=True, blank=True)

class HealthMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    steps = models.IntegerField()
    calories_burned = models.FloatField()

class HealthGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=100)
    target_value = models.FloatField()
    current_value = models.FloatField()
