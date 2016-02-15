from rest_framework import serializers
from hospital.models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=Hospital
		fields=('fullname','address','contactno','OPD','IPD','ICU','IICU','MRI','CTSCAN','XRAY','BloodTest')



