from django.contrib import admin


from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

CustomAccount = get_user_model()

class CustomAccountAdmin(UserAdmin):
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm
    model = CustomAccount
    list_display = ['email', 'username',]

admin.site.register(CustomAccount, CustomAccountAdmin)


