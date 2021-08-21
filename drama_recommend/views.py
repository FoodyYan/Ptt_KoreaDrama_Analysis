from django.shortcuts import render
from django.http import JsonResponse
import os
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.
def home(request):
    return render(request, 'drama_recommend/index.html')

def load_df_date():
    global df # global variable
    df = pd.read_csv('drama_recommend/dataset/PTTkoreadrama_hot.csv',sep='|',converters = {'date2':str})

load_df_date()

@csrf_exempt
def api_get_recommend(request):
    date = request.GET['date']
    response = get_latest_article(date)
    return JsonResponse({"koreadrama_recommend": response})

def get_latest_article(date):
    items = []
    df_date = df[df.date2 == date]

    df_date = df_date.head(5) 

    for i in range(len(df_date)):
        
        
        date_ = df_date.iloc[i].date2
        title = df_date.iloc[i].title
        link = df_date.iloc[i].url_link
        hot = df_date.iloc[i].hot
        
        item = {
            "date": date_,
            "title": title, 
            "link": link,
            "hot": '<font color="#FF0000">' + hot + '</font>'
            }
        items.append(item)

    if len(df_date) < 5:
        
        for i in range(5-len(df_date)):
            print(i)
            rd = random.randint(0, 1229)

            date_ = df.iloc[rd].date2
            title = df.iloc[rd].title
            link = df.iloc[rd].url_link
            hot = df.iloc[rd].hot
        
            item = {
                "date": date_,
                "title": title, 
                "link": link,
                "hot":'<font color="#FF0000">' + hot + '</font>'
            }
            items.append(item)


    return items

def call_me(request):
    return render(request, 'drama_recommend/'+request+'.html')

def tables(request):
    return render(request, 'drama_recommend/tables.html')

def charts(request):
    return render(request, 'drama_recommend/charts.html')