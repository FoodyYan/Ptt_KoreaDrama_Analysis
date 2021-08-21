from django.urls import path
from sentiment_analysis import views

app_name="namespace_sentiment_analysis"

urlpatterns = [
    path('', views.home, name = "home"),
    path('api_get_sentiment/', views.api_get_sentiment),
    path('api_get_voice/', views.api_get_voice),

]
