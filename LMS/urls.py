from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken import views as authviews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ckeditor_uploader.urls')),
    # path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
    path('api/v1/curriculum/', include('curriculum.urls')),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/student/', include('student.urls')),
    path('api/v1/', include('manager.urls')),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
