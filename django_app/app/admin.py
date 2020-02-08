from django.contrib import admin

# Register your models here.
from .models import MyModel, RichModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(RichModel)