
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers
from location import views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'locations', views.TrashcanViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('signup/',views.SignupView.as_view()),
    path('signin/',views.SigninView.as_view()),
    path('action/',views.TrashcanActionViewSet.as_view({'post': 'action'})),
    path('pin/', views.PinView.as_view({'get': 'list'})),
    path('check/', views.TrashcanCheckViewSet.as_view({'post': 'is_trashcan'})),
    path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls'))
    #path('api-auth/', include('rest_framework.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)