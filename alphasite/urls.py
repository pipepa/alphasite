"""
URL configuration for alphasite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from dashboard.views import loginuser, currentdasboard, home, logoutuser
admin.site.site_header = 'Адміністрування'
admin.site.site_title = 'Адміністрування'

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', loginuser, name='loginuser'),
    path('logoutuser/', logoutuser, name='logoutuser'),
    path('currentdasboard/', currentdasboard, name='currentdasboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)