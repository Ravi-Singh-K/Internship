from . import views
from django.urls import path


urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("edit_profile/", views.edit_view, name="edit"),
    path("update/", views.update, name="update"),
    path("Sample-1/", views.sample1, name="sample1"),
    path("Sample-2/", views.sample2, name="sample2"),
    path("Sample-3/", views.sample3, name="sample3"),
    path("download/", views.download, name="download"),
]