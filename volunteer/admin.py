from django.contrib import admin
from .models import Social,Education,Contact


class SocialAdmin(admin.ModelAdmin):
    list_display=('fname','lname','DOB','gender','Hostpital_name','Doctor_name','ownLaptop','ownVechile')

class EducationAdmin(admin.ModelAdmin):
    list_display=('school_name','school_yearofpassing','graduation','college_name','grad_yearofpassing')

class ContactAdmin(admin.ModelAdmin):
    list_display=('state','city','zone','address','contactno','alt_contactno')


admin.site.register(Social,SocialAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Contact,ContactAdmin)


# Register your models here.
