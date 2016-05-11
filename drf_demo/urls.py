from rest_framework import routers
from drf_demo.model_less.views import TaskViewSet, userlocviewset, groupviewset
from django.conf.urls import patterns, include, url 
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, base_name='tasks')
router.register(r'users', userlocviewset, base_name='users')
router.register(r'sets', groupviewset, base_name='sets')
urlpatterns = [ 
url(r'^', include(router.urls)),
url(r'^admin/', admin.site.urls),
]
