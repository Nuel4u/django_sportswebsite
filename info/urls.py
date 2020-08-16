from django.urls import path
from .import views 
#from .views import (
#    HomeView,
#)


#app_name ="info"


urlpatterns = [
   # path('' , HomeView.as_view() ,name="HomeView"),
    path('' , views.home ,name='home'),
    path('about/',views.about ,name='about'),
    path('mission/',views.about ,name='mission'),
    path('training/',views.about ,name='training'),
    path('registration/',views.about ,name='registration'),
    path('contact/',views.about ,name='contact'),
]


