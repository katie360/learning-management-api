from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'manager', views.ManagerViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('manager-dashboard/', views.ManagerDashboard),
]