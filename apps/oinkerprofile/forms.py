from django import forms
from .models import OinkerProfile

# this file generates a form that allows users to upload files/images: it is not an actual form for users to sign-up 
class OinkerProfileForm(forms.ModelForm):
    class Meta: 
        model = OinkerProfile
        fields = ('avatar', )