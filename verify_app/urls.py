from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('change-password-old/', views.pass_change_1, name='pass_change_1'),
    path('change-password-new/', views.pass_change_2, name='pass_change_2'),
]
