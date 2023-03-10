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
    path('student-timetable/', views.get_student_timetable, name='get_student_timetable'),
    path('student-announcements/', views.get_student_announcements, name='get_student_announcements'),
    path('student-announcement-detail/<int:id>/', views.get_student_announcement_detail, name='get_student_announcement_detail'),
    path('student-exams/', views.get_student_exams, name='get_student_exams'),
    path('student-ask-question/', views.student_ask_question, name='student_ask_question'),
]
