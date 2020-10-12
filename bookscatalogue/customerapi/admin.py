from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import CustomerProfile

class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = CustomerProfile
    list_display = ['first_name', 'email', 'username', 'country']

admin.site.register(CustomerProfile, UserProfileAdmin)