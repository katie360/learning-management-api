from django.urls import include, path
from rest_framework import routers
from . import views
from knox import views as knox_views


router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('login/', views.LoginAPI.as_view(), name='login'),
   path('signin/', views.login_api, name='signin'),
   path('user/', views.get_user_data, name='get_user_data'),
   path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
   path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]