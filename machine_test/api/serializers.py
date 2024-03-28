from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

from rest_framework import serializers
#from rest_framework.validators import CurrentUserDefault
from rest_framework.fields import CurrentUserDefault
from .models import Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

"""class ClientSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Client
        fields = '__all__' """


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    users = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    #created_by_display = serializers.SerializerMethodField(read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by',  'projects'] #'created_by_display',

    def get_created_by_display(self, obj):
        return obj.created_by.username if obj.created_by else None
