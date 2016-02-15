from rest_framework import serializers
from userprofile.models import UsersProfile



class UsersProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=UsersProfile
		fields=('id','username','password','emailid','usergroup','sessions','status','online','mobileno','createdate','img')


		
