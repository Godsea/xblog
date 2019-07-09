from django.urls import path
from .views import index,index_blog

urlpatterns = [
    path('',index),
    path('<int:nav_id>/<int:con_id>/<int:blog_pk>/',index_blog),
    path('<int:nav_id>/',index),
]
