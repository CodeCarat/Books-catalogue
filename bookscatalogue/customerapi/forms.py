from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerProfile

class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = CustomerProfile
        fields = ('username', 'first_name', 'email', 'country')

class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = CustomerProfile
        fields = UserChangeForm.Meta.fields

        