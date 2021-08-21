from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'dataframe/index.html')


def load_df_data():
    global df # global variable
    df = pd.read_csv('dataframe/dataset/PTTkoreadrama_for_django.csv',sep='|')

load_df_data()

@csrf_exempt
def api_ptt_df_all(request):
    response = get_PTT_df()
    return JsonResponse({"data": response})


def get_PTT_df():
    items = []

    for i in range( len(df)):
        title = df.iloc[i].title
        link = df.iloc[i].link
        date = df.iloc[i].date
        content = df.iloc[i].content

        item = {
            "title": '<a href="' + link + '">' + title + '</a>',
            "link": link,
            "date": date,
            "content": content[0:100] + "...",
        }

        items.append(item)
    
    return items