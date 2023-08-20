from . import views
from django.urls import path
app_name='main'
urlpatterns = [
    # /food/
    path('',views.main,name='main'),
    path('index/',views.index_main,name='index_main'),
    path('login_0/',views.login_0,name="login_0"),
    path('about/',views.about,name="about"),
    path('cleaner/',views.cleaner,name="cleaner"),
    path('cook/',views.cook,name="cook"),
    path('plumber/',views.plumber,name="plumber"),
    path('elec/',views.elec,name="elec"),
    path('carp/',views.carp,name="carp"),
]