"""
URL configuration for qr_code_project project.

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
from django.contrib import admin
from django.urls import path, include
from QRC.views import GenerateQRView, UserQRCodeListView, RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-qr/', GenerateQRView.as_view(), name='generate-qr'),
    path('user/qr-codes/', UserQRCodeListView.as_view(), name='user-qr-codes'),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('QRC/', include('QRC.urls')),
]
