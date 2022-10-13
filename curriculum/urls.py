from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'curriculum', views.CurriculumViewSet)
router.register(r'class', views.ClassViewSet)
router.register(r'subject', views.SubjectViewSet)
router.register(r'resource', views.ResourceViewSet)



urlpatterns = [
   path('', include(router.urls)),
   path('curriculum/', views.get_curriculum, name='get_curriculum'),
   path('resources/', views.get_resources, name='get_resources'),
   path('resource-chapters/<str:pk>/', views.get_resource_chapters, name='get_resource_chapters'),
   path('single-resource-chapter/<str:pk>/', views.get_single_resource_chapter, name='get_resource_chapter'),
   path('resource-textbooks-free/', views.get_resource_textbooks_free, name='get_resource_textbooks_free'),
   path('resource-textbooks-paid/', views.get_resource_textbooks_paid, name='get_resource_textbooks_paid'),
   path('asked-questions/', views.get_asked_questions, name='asked_questions'),
   path('general-timetable/', views.get_general_timetable, name='general_timetable'),
   path('assignments/', views.get_assignments, name='assignments'),
]
