"""
URL configuration for project25 project.

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
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topics/',display_topics,name="display_topics"),
    path('insert_topic/',insert_topic,name="insert_topic"),
    path('display_webpages/',display_webpages,name="display_webpages"),
    path('insert_webpage/',insert_webpage,name="insert_webpage"),
    path('display_access_records/',display_access_records,name="display_access_records"),
    path('Insert_Access_Records/',Insert_Access_Records,name="Insert_Access_Records"),
    path('update_webpages/',update_webpages,name="update_webpages"),
    path('delete_Access_Records/',delete_Access_Records,name="delete_Access_Records"),
]
