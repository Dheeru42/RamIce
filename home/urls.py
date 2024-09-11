from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('about',views.about,name='about'),
    path('contactus',views.contact,name='contact')
]
