from rest_framework import serializers
from patient.models import SocialInfo,HealthInfo,FinancialInfo,ContactInfo


class SocialInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=SocialInfo
		fields=('firstname','lastname','dob','contactno','fathername','fdob','fcontactno','mothername','mdob','mcontactno','gender','siblings','spousename','sdob','marriagedate','children','girlcount','birthplace','delivery','domicile','yearofliving','custom_id')



class HealthInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=HealthInfo
		fields=('Allergy','PhysicalChallenged','BloodGroup','HomeAddress','ChronicDisease1','TroubleDisease1','Digestion','Diagnosed','Preference')


class FinancialInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=FinancialInfo
		fields=('LivingStandard','OwnLand','OwnVechile','Occupation','AnnualIncome','BankAccount','Loan1','Loan2','Loan3','ssi','remark','emailID')

class ContactInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=ContactInfo
		fields='__all__'