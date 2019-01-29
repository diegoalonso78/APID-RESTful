from django.urls import path

from . import views

app_name = 'interactions'
urlpatterns = [
    path('<slug:protein_id>/', views.oneProtein, name='oneProtein'),
    path('<slug:participant1_id>/<slug:participant2_id>/', views.twoProteins, name='twoProteins'),
]