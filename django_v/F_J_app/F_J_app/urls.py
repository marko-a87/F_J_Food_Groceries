"""
URL configuration for F_J_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "F_J_app.settings")
application = get_wsgi_application()

from django.contrib import admin
from django.urls import path, include
from F_J_app.views import Login as view
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings
from .import views
 
urlpatterns = [
 
    path('admin/', admin.site.urls),
 
    ##### user related path########################## 
    path('', include('user.urls')),
    path('login/', view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', view.register, name ='register'),
]
urlpatterns = [
    path('', views.index, name ='index'), 
]

