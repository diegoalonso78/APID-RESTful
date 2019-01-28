from django.urls import path

from . import views

app_name = 'protein'
urlpatterns = [
    path('<slug:protein_id>/', views.index, name='index'),
]