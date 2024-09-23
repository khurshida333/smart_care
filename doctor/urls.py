from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter() #the router maps URLs to the appropriate viewset actions .list(), .create(), .retrieve(), etc.
router.register('specialization', views.SpecializationViewset)
router.register('list', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('available_time', views.AvailableTimeViewset)
router.register('review', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]