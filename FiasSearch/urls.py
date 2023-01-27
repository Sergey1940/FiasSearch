from django.contrib import admin
from django.urls import path, include

from fiascheck.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'fias', FiasViewSet, basename='fias')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('fiascheck.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v2/fiaslist/', FiasAPIView2.as_view()),
]
