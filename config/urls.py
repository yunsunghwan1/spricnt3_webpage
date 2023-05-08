from django.urls import path, include
from django.contrib import admin
from mainapp import views 
urlpatterns = [
    # path('', views.index), 
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
]
