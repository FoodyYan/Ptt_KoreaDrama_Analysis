"""website_configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.urls import path
from django.urls import include

urlpatterns = [
    # analysis
    path('drama_recommend/', include('drama_recommend.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dataframe/', include('dataframe.urls')),
    path('sentiment_analysis/', include('sentiment_analysis.urls')),

]
