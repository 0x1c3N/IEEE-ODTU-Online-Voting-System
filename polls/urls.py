from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings



app_name = "user"

urlpatterns = [
    path('',views.index1),
    path('<int:question_id>/',views.detail,name = "detail"),
    path('<int:question_id>/vote',views.vote,name = "vote"),
    
] 
