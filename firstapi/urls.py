from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('languages',views.ModelViewSet)
router.register('paradigm', views.ParadigmviewwSet)
router.register('paradigm', views.ProgrammerViewSet)
urlpatterns = [
    path('',include(router.urls))
]