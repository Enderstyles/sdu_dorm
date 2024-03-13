from django.contrib import admin
from .models import AboutPiece, CustomUser, MainPageModel, NewsPost, NewsCategories

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AboutPiece)
admin.site.register(MainPageModel)
admin.site.register(NewsPost)
admin.site.register(NewsCategories)
