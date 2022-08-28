from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    # path('userreg',views.userreg,name='userreg'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userlogin2', views.userlogin2, name='userlogin2'),
    path('logout',views.logout,name='logout'),

]