from django.contrib import admin
from .models import CustomUser, Equipment, Data, Alert

admin.site.register(CustomUser)
admin.site.register(Equipment)
admin.site.register(Data)
admin.site.register(Alert)
