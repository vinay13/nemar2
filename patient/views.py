#from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from patient.models import SocialInfo,HealthInfo,FinancialInfo,ContactInfo
from patient.serializers import SocialInfoSerializer,HealthInfoSerializer,FinancialInfoSerializer,ContactInfoSerializer

# Create your views here.


@api_view(['GET','POST'])
def socialinfo(request):
	if request.method == 'GET' :
		health5=SocialInfo.objects.all()
		serializer=SocialInfoSerializer(health5,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=SocialInfoSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def healthinfo(request):
	if request.method == 'GET' :
		health6=HealthInfo.objects.all()
		serializer=HealthInfoSerializer(health6,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer=HealthInfoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)		




@api_view(['GET','POST'])
def financialinfo(request):
	if request.method == 'GET' :
		health7=FinancialInfo.objects.all()
		serializer=FinancialInfoSerializer(health7,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer=FinancialInfoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def contactinfo(request):
	if request.method == 'GET' :
		contact=ContactInfo.objects.all()
		serializer=ContactInfoSerializer(contact,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer=ContactInfoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)







