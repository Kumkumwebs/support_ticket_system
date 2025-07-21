from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, SocialAccount


# ✅ Registration Form for new users
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# ✅ Profile Form (Edit Profile)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['twitter_username', 'facebook_username', 'profile_picture']


# ✅ Social Media Handles Form
class SocialAccountForm(forms.ModelForm):
    class Meta:
        model = SocialAccount
        fields = ['twitter_handle', 'facebook_handle']
