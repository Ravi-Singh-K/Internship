from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("user-login/", views.do_login, name="log-in"),
    path("user-dashboard/", views.dashboard, name="dashboard"),
    path("user-logout/", views.do_logout, name="log-out"),
    path("user-update/", views.do_update, name="update"),
    path("personal-information/", views.personalinfo, name="personalinfo"),
    path("education-update/", views.update_education, name="update_education"),
    path("work-experience-update/", views.update_work_experience, name="update_experience"),
    path("update-links/", views.update_link, name="update_link"),
    path("update-achievement/", views.update_achievement, name="update_achievement"),
    path("update-references/", views.update_reference, name="update_reference"),

    path("update-skill/", views.update_skill, name="update_skill"),
    path('skills/edit/<int:skill_id>/', views.edit_skill, name='edit_skill'),

    path("update-language/", views.update_language, name="update_language"),
    path('languages/edit/<int:language_id>/', views.edit_language, name='edit_language'),

    path("download/", views.download, name="download"),

    path("sample1/", views.sample1, name="sample1"),
    path("sample2/", views.sample2, name="sample2"),
    path("sample3/", views.sample3, name="sample3"),
]