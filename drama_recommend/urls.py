from django.urls import path
from drama_recommend import views

app_name="namespace_drama_recommend"

urlpatterns = [
    path('', views.home, name = "home"),
    path('api_get_recommend/',views.api_get_recommend),
    path('tables', views.tables, name = "tables"),
    path('charts', views.charts, name = "charts"),
]
