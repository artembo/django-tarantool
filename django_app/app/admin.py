from django.contrib import admin

from . import models


admin.site.register(models.AllModel)
admin.site.register(models.Float)
admin.site.register(models.Decimal)
admin.site.register(models.BigInteger)
admin.site.register(models.Integer)
admin.site.register(models.SmallInteger)
admin.site.register(models.PositiveInteger)
admin.site.register(models.PositiveSmallInteger)
admin.site.register(models.Boolean)
admin.site.register(models.NullBoolean)

@admin.register(models.DateTime)
class DateTimeAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time_auto',)

admin.site.register(models.Date)
admin.site.register(models.Time)


@admin.register(models.Char)
class CharAdmin(admin.ModelAdmin):
    list_per_page = 5


admin.site.register(models.Text)
admin.site.register(models.GenericIPAddress)
admin.site.register(models.File)
admin.site.register(models.FilePath)
admin.site.register(models.OneToOne)


@admin.register(models.OneToOneRelative)
class OneToOneRelative(admin.ModelAdmin):
    readonly_fields = ('id',)
