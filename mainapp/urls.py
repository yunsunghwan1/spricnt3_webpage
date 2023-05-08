from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),

    ### 전력 사용Population_power
    path('Population_PowerPlant/', views.Population_PowerPlant),

    path('Population_consumption/', views.Population_consumption),


    ### 비동기 사진 보기  

]
