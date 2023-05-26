from django.urls import path 
from .views import * 

app_name = 'post' 

urlpatterns = [
    path('', all, name='all'),
    path('<int:id>/', single_post, name='single-post'), 
]
