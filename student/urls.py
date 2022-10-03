from django.urls import include, path
from rest_framework import routers
from . import views
from knox import views as knox_views


router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('student-user/', views.get_student_data, name='get_student_data'),
    path('subjects-enrolled/', views.get_subjects_enrolled, name='get_subjects_enrolled'),
   
]
