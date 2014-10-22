from django.contrib import admin
from analytics.models import View, Location, Page

admin.site.register(Page)
admin.site.register(Location)
admin.site.register(View)

