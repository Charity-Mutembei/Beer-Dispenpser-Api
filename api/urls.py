from django.urls import path
from api.infrastructure import views


app_name = 'api'

urlpatterns = [
    path('beer-tap/', views.home, name="home"),
    path('dispenses-api/', views.DispenseList.as_view(), name="api-list"), 

]
