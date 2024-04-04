from django.urls import path
from .views import index, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
]