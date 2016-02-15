from rest_framework import serializers
from health.models import Bloodpressurechart,Meanbloodglucose,DoctorList,MedicalOperate


class BloodpressurechartSerializer(serializers.ModelSerializer):
	class Meta:
		model=Bloodpressurechart
		fields=('Age','Min','Normal','Max')


class MeanbloodglucoseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Meanbloodglucose
		fields=('Level','mgDL','nmolL','Risk','suggested_action')

"""

class RegionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Region
		fields=('id','region','parent_id','region_type','coordinate','region_order','pincode','publish')

"""

class DoctorListSerializer(serializers.ModelSerializer):
	class Meta: 
		model=DoctorList
		fields=('id','name','home_address','hospital_address','clinic_address','contact_no')



 
class MedicalOperateSerializer(serializers.ModelSerializer):
	class Meta:
		model=MedicalOperate
		fields=('id','operate_name','operate_type')



class SocialInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=SocialInfo
		fields=('FirstName','LastName','Dob','ContactNo','FatherName','fDOB','fContactNo','MotherName','mDOB','mContactNo','Gender','siblings','SpouseName','sDOB','MarriageDate','Children','GirlCount','BirthPlace','Delivery','Domicile','YearOfLiving')



class HealthInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=HealthInfo
		fields=('Allergy','PhysicalChallenged','BloodGroup','HomeAddress','ChronicDisease1','TroubleDisease1','Digestion','Diagnosed','Preference')


class FinancialInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=FinancialInfo
		fields=('LivingStandard','OwnLand','OwnVechile','Occupation','AnnualIncome','BankAccount','Loan1','Loan2','Loan3','ssi','remark','emailID')

