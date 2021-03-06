"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from app1.views import *
from views import commonviews
from django.contrib.auth.views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',commonviews.welcome),
    url(r'^login$',view=login,name="login",kwargs={'template_name':'registration/login.html'}),
    url(r'^logout$',view=logout,name="logout",kwargs={'template_name':'registration/login.html'}),
    #url(r'^welcome/',view=welcome,name='welcome'),
    url(r'^signup/',TemplateView.as_view(template_name='registration/register.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
