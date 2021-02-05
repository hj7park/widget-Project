from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('widgets/add', views.createWidget.as_view(), name='addWidget'),
    path('widgets/delete/<int:pk>', views.deleteWidget.as_view(), name='deleteWidget'),
]