#from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from volunteer.models import Social,Education,Contact
from volunteer.serializers import SocialSerializer,EducationSerializer,ContactSerializer



@api_view(['GET','POST'])
def social(request):
	if request.method == 'GET':
		health=Social.objects.all()
		serializer=SocialSerializer(health,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=SocialSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET', 'PUT', 'DELETE'])
def social_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        social_d = UsersProfile.objects.get(pk=pk)
    except UsersProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersProfileSerializer(social_d)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersProfileSerializer(social_d, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        social_d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','POST'])
def education(request):
	if request.method == 'GET':
		health=Education.objects.all()
		serializer=EducationSerializer(health,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=EducationSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 



@api_view(['GET', 'PUT', 'DELETE'])
def education_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        uesrprof2 = UsersProfile.objects.get(pk=pk)
    except UsersProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersProfileSerializer(uesrprof2)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersProfileSerializer(uesrprof2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uesrprof2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET','POST'])
def contact(request):
	if request.method == 'GET':
		health=Contact.objects.all()
		serializer=ContactSerializer(health,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=ContactSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        uesrprof3 = UsersProfile.objects.get(pk=pk)
    except UsersProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersProfileSerializer(uesrprof3)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersProfileSerializer(uesrprof3, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uesrprof3.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# Create your views here.
