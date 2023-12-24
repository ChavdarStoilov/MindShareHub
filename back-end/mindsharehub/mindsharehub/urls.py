from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('rest-api/', include('apps.rest_api.urls')),
    path('', include('apps.render_app.urls')),
    
    path('auth/', include('apps.auth_app.urls'), name="auth_applications_urls"),
    
]
