from django.urls import path, include
from rest_framework import routers
from Userapp.views import UserViewset, ProfileViewset

router = routers.DefaultRouter()
router.register('user', UserViewset)
# router.register('profile', ProfileViewset)

urlpatterns = [
    path('', include(router.urls),)
 ]