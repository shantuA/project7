from django.urls import path
from csk.views import *
app_name="cskteam"
urlpatterns=[

    path('msd/',msd,name='msd'),
]