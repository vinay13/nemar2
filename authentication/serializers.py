from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account,UserGroup


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserGroup
        fields='__all__'


        
class AccountSerializer(serializers.ModelSerializer):
    group = serializers.IntegerField(required=True)
    first_name = serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = '__all__'
        #exclude=('user_permissions',)
        #depth = 1
        read_only_fields = ('created_at', 'updated_at',)

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance




