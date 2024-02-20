from django.contrib import admin
from .models import AboutPiece, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AboutPiece)
