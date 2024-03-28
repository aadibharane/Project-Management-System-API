from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet 
from api import views
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/',views.CreateClientAPIView.as_view(),name='client_create'),
    
]
