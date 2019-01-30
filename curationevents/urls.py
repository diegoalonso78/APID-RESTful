from django.urls import path

from . import views

app_name = 'curationevents'
urlpatterns = [
    path('<slug:participant1_id>/<slug:participant2_id>/', views.twoProteins, name='twoProteins'),
]