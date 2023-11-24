from django.urls import path
from population import views

urlpatterns = [
    path("",views.SignUpView.as_view(),name="signup"),
    path("signin/",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("population/",views.PopulationCreateView.as_view(),name="population"),
    path('search/',views.search_view.as_view(), name='search'),
    path("population/<int:pk>/",views.PopulationDetailView.as_view(),name="detail-population"),
    path("population/<int:pk>/change",views.PopulationUpdateView.as_view(),name="change-population"),
    path("population/<int:pk>/remove",views.remove_population,name="remove-population"),
    path("signout/",views.signout_view,name="signout"),
]
