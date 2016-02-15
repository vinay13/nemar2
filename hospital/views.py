from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from hospital.models import Hospital
from hospital.serializers import HospitalSerializer



@api_view(['GET','POST'])
def hospital(request):
	if request.method == 'GET':
		hospital=Hospital.objects.all()
		serializer=HospitalSerializer(hospital,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=HospitalSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

# Create your views here.
