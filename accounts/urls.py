from django.urls import path,include
from .views import Signupview

urlpatterns = [
    path("signup/",Signupview.as_view(),name="signup"),
]


