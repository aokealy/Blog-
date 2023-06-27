from django.contrib import admin
from .models import EmailContact

# Register your models here.

@admin.register(EmailContact)
class EmailContactAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "topic",
    )

