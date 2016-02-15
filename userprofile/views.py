from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userprofile.models import UsersProfile
from userprofile.serializers import  UsersProfileSerializer



# Create your views here.
@api_view(['GET','POST'])
def userprofile(request):
	if request.method == 'GET' :
		uesrprof1=UsersProfile.objects.all()
		serializer=UsersProfileSerializer(uesrprof1,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=UsersProfileSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def userprofile_detail(request, pk):
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



"""

#This below code works for user Login authentication
#it checks username n password .. whether it exists or not 
#if not generate a error 
@api_view(['GET'])
def userprofile_login(request,username):

    try:
        username = UsersProfile.objects.get(username=username)
#        if username.password == True:
#            return Response({"yehh valid authentication"})
#        else:
#            return Response({"incorrect password"})

    except UsersProfile.DoesNotExist:
        return Response({"Username Not Found"})
"""


# Create your views here.
# Create your views here.
