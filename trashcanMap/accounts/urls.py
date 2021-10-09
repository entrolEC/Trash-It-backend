from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from accounts.views import UserViewSet
from accounts import views

router = routers.DefaultRouter()
router.register('/user', UserViewSet)

urlpatterns = [
  path('google/login', views.google_login),
  path('google/callback/', views.google_callback,      name='google_callback'),  
  path('accounts/google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
  path('', include('dj_rest_auth.urls')),
  path('', include('dj_rest_auth.registration.urls')),
  path('', include('allauth.urls')),
  path('', include(router.urls)),
  #path('', include('accounts.urls')),
]