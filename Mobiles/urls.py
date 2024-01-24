"""
URL configuration for Mobiles project.

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
from app.views import MobileView,MobileList,Mobiledetails,Mobileremove,Mobileupdate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MobileView.as_view(),name="add"),
    path('list/',MobileList.as_view(),name="lst"),
    path('details/<int:pk>',Mobiledetails.as_view(),name="det"),
    path('list/<int:pk>/remove',Mobileremove.as_view(),name="rem"),
    path('list/<int:pk>/edit',Mobileupdate.as_view(),name="edit")
]

