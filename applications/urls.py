from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/login/", auth_views.LoginView.as_view()),
    path("applications", views.apps.as_view(), name="applications"),
    path("apps", views.apps.as_view(), name="apps"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]