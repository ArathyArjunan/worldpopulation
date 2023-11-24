from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("population",views.PopulationView,basename="population")
urlpatterns = [
    
    path("user/me/",views.UserView.as_view()),
    path("token/",ObtainAuthToken.as_view())
]+router.urls
