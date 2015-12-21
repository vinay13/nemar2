from rest_framework import serializers
from health.models import Bloodpressurechart,Meanbloodglucose,Region


class BloodpressurechartSerializer(serializers.ModelSerializer):
	class Meta:
		model=Bloodpressurechart
		fields=('Age','Min','Normal','Max')


class MeanbloodglucoseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Meanbloodglucose
		fields=('Level','mgDL','nmolL','Risk','suggested_action')



class RegionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Region
		fields=('id','region','parent_id','region_type','coordinate','region_order','pincode','publish')
