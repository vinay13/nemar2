from django.contrib import admin
from .models import MedicalOperate,DoctorList,Meanbloodglucose,Bloodpressurechart,Cholestrolriskchart

class MeanbloodglucoseAdmin(admin.ModelAdmin):
    list_filter=('Level','mgDL','nmolL','Risk')
    list_display=('Level','mgDL','nmolL','Risk')
    search_fields=['Level','Risk']


"""
class RegionAdmin(admin.ModelAdmin):
    list_display=('id','region','parent_id','region_type','coordinate','region_order','publish')
    list_filter=('region_type',)
    search_fields=('region','parent_id')
"""

class BloodpressurechartAdmin(admin.ModelAdmin):
    list_display=('Age','Min','Normal','Max')
    list_filter=('Age','Max')
    search_fields=('Age','Max') 


class DoctorListAdmin(admin.ModelAdmin):
    list_display=('id','name','home_address','clinic_address','contact_no')




#class SpecializeAdmin(admin.ModelAdmin):
#    list_display=('id','sname')


class MedicalOperateAdmin(admin.ModelAdmin):
    list_display=('id','operate_name','operate_type')
    list_filter=('operate_type',)


class SocialInfoAdmin(admin.ModelAdmin):
    list_display=('FirstName','LastName','Dob')

class CholestrolriskchartAdmin(admin.ModelAdmin):
    list_display=('Age','C150','C151to160','C161to170','C171to180','C181to190','C191to200','C201to210','C211to220','C221to230')

admin.site.register(Meanbloodglucose,MeanbloodglucoseAdmin)
admin.site.register(Bloodpressurechart,BloodpressurechartAdmin)
#admin.site.register(Region,RegionAdmin)
admin.site.register(Cholestrolriskchart,CholestrolriskchartAdmin)
admin.site.register(DoctorList,DoctorListAdmin)
#admin.site.register(Specialize,SpecializeAdmin)
admin.site.register(MedicalOperate,MedicalOperateAdmin)
#admin.site.register(SocialInfo,SocialInfoAdmin)
# Register your models here.
