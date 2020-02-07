from django.contrib import admin

# Register your models here.
from .models import MyModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
