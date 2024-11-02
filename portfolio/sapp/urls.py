from django.urls import path
from .views import GenerateQRView, UserQRCodeListView, RegisterView, LoginView, AccountView, home, about, signup, login, account, api

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('account/', account, name='account'),
    path('api/', api, name='api'),
    path('generate-qr/', GenerateQRView.as_view(), name='generate-qr'),
    path('user/qr-codes/', UserQRCodeListView.as_view(), name='user-qr-codes'),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(), name='api-login'),
    path('user/account/', AccountView.as_view(), name='account-details'),
]