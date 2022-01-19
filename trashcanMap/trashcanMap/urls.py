
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from location import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('location.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)