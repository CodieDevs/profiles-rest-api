from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
     path('get_view/', views.HelloApiView.as_view()),
     path('', include(router.urls))
]
