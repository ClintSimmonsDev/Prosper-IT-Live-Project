from . import views
from django.urls import path
from django.views import static

urlpatterns = [
    path('', views.Airport_Code_Index, name="Airport_Code_Index"),
    path('city_search', views.city_search, name="city_search"),
    # path('code_search', views.code_search, name="code_search"),
]