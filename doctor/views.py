from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from doctor.models import DoctorInfo
from doctor.serializers import DoctorInfoSerializer



@api_view(['GET','POST'])
def doctorinfo(request):
	if request.method == 'GET':
		doctor=DoctorInfo.objects.all()
		serializer=DoctorInfoSerializer(doctor,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=DoctorInfoSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 




# Create your views here.
