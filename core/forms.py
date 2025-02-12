from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'dietary_habits', 'exercise_routines']
