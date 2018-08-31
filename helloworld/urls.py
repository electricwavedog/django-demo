"""helloworld URL Configuration

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
from hello import views as hello_views
from . import testdb
from testD import views as test_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello_views.hello),
    url(r'^testdb/$', testdb.testdb),
    url(r'^index/$', hello_views.index, name='home'),
    url(r'^test/$', test_views.toPage, include('rest_framework.urls', namespace='rest_framework')),
    url(r'^update$', test_views.update),
]
