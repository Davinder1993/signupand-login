
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('user-login',views.userlogin,name='user_login'),
    path('sign-out',views.signout,name='sign_out'),
    path('profile',views.profile,name="profile"),
    path('profile-edit',views.profile_edit,name='profile_edit')

]