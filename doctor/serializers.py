from rest_framework import serializers
from doctor.models import DoctorInfo


class DoctorInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DoctorInfo
		fields=('id','fullname','specialize','experience','region','contact_no','home_address','hospital_address','clinic_address')



