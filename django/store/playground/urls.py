from django.urls import path, include
from . import views

urlpatterns =[
    path('playground/hello/', views.say_hello),
    path('playground/', include('playground.urls'))
]
