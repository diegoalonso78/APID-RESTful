from django.urls import path

from . import views

app_name = 'publication'
urlpatterns = [
    path('<slug:pubmed_id>/', views.index, name='index'),
]