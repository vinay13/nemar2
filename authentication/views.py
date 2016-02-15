from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from authentication.models import Account,UserGroup
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer,UserGroupSerializer
from django.contrib.auth import logout
from rest_framework import permissions
import json
from django.contrib.auth import authenticate, login
from rest_framework import status, views
#from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def groupdetails(request):
    request.session.set_test_cookie()
    if request.method == 'GET':
        jobdetails=UserGroup.objects.all()
        serializer=UserGroupSerializer(jobdetails,many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer=UserGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 




class AccountViewSet(viewsets.ModelViewSet):
   # request.session.set_test_cookie()
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.



class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)





class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)            


