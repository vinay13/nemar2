from django.contrib import admin
from .models import Hospital



class HospitalAdmin(admin.ModelAdmin):
	list_display=('fullname','address','contactno','OPD')




admin.site.register(Hospital,HospitalAdmin)



# Register your models here.
