from django.contrib import admin
from .models import AboutPost, CustomUser, MainPageModel, NewsPost, NewsCategories, Enrollment, TakenPlaces, Gender, \
    PaymentModel, UploadDocumentsModel, CitizenshipModel, BookingStatus

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AboutPost)
admin.site.register(MainPageModel)
admin.site.register(NewsPost)
admin.site.register(NewsCategories)
admin.site.register(Enrollment)
admin.site.register(TakenPlaces)
admin.site.register(Gender)
admin.site.register(PaymentModel)
admin.site.register(UploadDocumentsModel)
admin.site.register(CitizenshipModel)
admin.site.register(BookingStatus)