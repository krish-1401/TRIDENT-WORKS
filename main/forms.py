from django import forms
from .models import Profile

class Profile_form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['user_name','email','mobile','profession']