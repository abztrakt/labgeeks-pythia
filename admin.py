from django.contrib import admin
from labgeeks_pythia.models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Page, PageAdmin)
