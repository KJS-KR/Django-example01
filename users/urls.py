from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("survey", views.go_survey, name="survey"),
    path("survey/success", views.go_success, name="success"),
]
