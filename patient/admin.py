from django.contrib import admin
from .models import SocialInfo


class SocialInfoAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','dob')




admin.site.register(SocialInfo,SocialInfoAdmin)



# Register your models here.
