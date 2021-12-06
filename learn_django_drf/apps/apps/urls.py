from django.urls import include, path
from django.contrib import admin

import frontend.views

urlpatterns = [
    path('', frontend.views.home),
    path('cars_cbv/', include('cars_cbv.urls')),
    path('cars_fbv/', include('cars_fbv.urls')),
    path('cars_fbv_user/', include('cars_fbv_user.urls')),
    path('cars_gcbv_user/', include('cars_gcbv_user.urls')),

    # Enable built-in authentication views
    path('accounts/', include('django.contrib.auth.urls')),    
    # Enable built-in admin interface
    path('admin/', admin.site.urls),
]
