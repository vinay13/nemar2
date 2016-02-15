from rest_framework import serializers
from volunteer.models import Social,Education,Contact


class SocialSerializer(serializers.ModelSerializer):
	class Meta:
		model=Social
		fields=('fname','lname','DOB','gender','Hostpital_name','Doctor_name','ownLaptop','ownVechile')



class EducationSerializer(serializers.ModelSerializer):
	class Meta:
		model=Education
		fields=('school_name','school_yearofpassing','graduation','college_name','grad_yearofpassing')



class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model=Contact
		fields=('state','city','zone','address','contactno','alt_contactno')

