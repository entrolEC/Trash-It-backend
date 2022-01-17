from django.urls import path
from location import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'locations', views.TrashcanViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('signup/',views.SignupView.as_view()),
    #path('signin/',views.SigninView.as_view()),
    path('action/',views.TrashcanActionViewSet.as_view({'post': 'action'})),
    path('pin/', views.PinView.as_view({'get': 'list'})),
    path('check/', views.TrashcanCheckViewSet.as_view({'post': 'is_trashcan'})),
]