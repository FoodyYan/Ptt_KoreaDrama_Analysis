from django.urls import path
from dataframe import views

app_name="namespace_dataframe"

urlpatterns = [
    path('', views.home, name = "home"),
    path( "api_ptt_df_all/", views. api_ptt_df_all),

]
