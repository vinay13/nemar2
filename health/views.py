from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from health.models import Bloodpressurechart,Meanbloodglucose,Region
from health.serializers import BloodpressurechartSerializer,MeanbloodglucoseSerializer,RegionSerializer




def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")



@api_view(['GET','POST'])
def bloodpressurechart(request):
	if request.method == 'GET':
		health=Bloodpressurechart.objects.all()
		serializer=BloodpressurechartSerializer(health,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=BloodpressurechartSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 



@api_view(['GET','POST'])
def meanbloodglucose(request):
	if request.method == 'GET':
		health1=Meanbloodglucose.objects.all()
		serializer=MeanbloodglucoseSerializer(health1,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
	    serializer=	MeanbloodglucoseSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	    	


@api_view(['GET','POST'])
def region(request):
	if request.method == 'GET' :
	    health2=Region.objects.all()
	    serializer=RegionSerializer(health2,many=True)
	    return Response(serializer.data)

	elif request.method == 'POST' :
	    serializer=RegionSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)         


# Create your views here.
