from django.contrib import admin

from .models import Fias


class FiasAdmin(admin.ModelAdmin):
    list_display = ("Houseid", "Houseguid",)


admin.site.register(Fias, FiasAdmin)