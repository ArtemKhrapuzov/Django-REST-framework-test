from django.contrib import admin
from django.urls import path, include
from women.views import *
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    router = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]


router = MyCustomRouter()
router.register(r'women', WomenViewSet, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/
]
