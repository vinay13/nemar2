#from django.contrib import admin
from django.contrib import admin
from .models import UsersProfile,UserGroup,UserGroupCustom


class UsersProfileAdmin(admin.ModelAdmin):
    list_display=('id','username','password','emailid','usergroup','sessions','status','online','mobileno','createdate')

"""
class UserGroupAdmin(admin.ModelAdmin):
    list_display=('school_name','school_yearofpassing','graduation','college_name','grad_yearofpassing')

class UserGroupCustomAdmin(admin.ModelAdmin):
    list_display=('state','city','zone','address','contactno','alt_contactno')


admin.site.register(UsersProfile,UsersProfileAdmin)
admin.site.register(UserGroup,UserGroupAdmin)
admin.site.register(UserGroupCustom,UserGroupCustomAdmin)
"""

admin.site.register(UsersProfile,UsersProfileAdmin)

# Register your models here.
