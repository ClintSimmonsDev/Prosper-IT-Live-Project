from . import views
from django.contrib import admin
from django.urls import path, include
from django.views import static


urlpatterns = [
    path('', views.Travelogue_index, name="Travelogue_index"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<category>/", views.Travelogue_category, name="Travelogue_category"),
]