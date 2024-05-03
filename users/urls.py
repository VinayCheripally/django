from django.urls import path
from .import views

urlpatterns=[
    path("",views.home),
    path("logout",views.logout_view),
    path("login",views.login_view,name="login"),
    path("essayevaluator",views.essayevaluator,name="essayevaluator"),
    path("signup",views.signup)
]