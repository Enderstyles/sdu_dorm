from django.contrib import admin
from .models import AboutPost, CustomUser, MainPageModel, NewsPost, NewsCategories

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AboutPost)
admin.site.register(MainPageModel)
admin.site.register(NewsPost)
admin.site.register(NewsCategories)
