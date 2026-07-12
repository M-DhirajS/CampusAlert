from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("alerts/", views.alerts_page, name="alerts"),
    path("create-alert/", views.create_alert, name="create_alert"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("history/", views.history, name="history"),
    path("profile/", views.profile, name="profile"),
]