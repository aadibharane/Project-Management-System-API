from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.generics import CreateAPIView

class ClientViewSet(viewsets.ModelViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        #user = self.request.user
        #return Project.objects.filter(users=user)
        return Project.objects.all()
    
