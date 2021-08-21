from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
import json
# Create your views here.


def home(request):
    return render(request, 'sentiment_analysis/index.html')


def load_df_data():
    global df  # global variable
    #df = pd.read_csv('dataset/news_dataset_preprocessed_for_django.csv',sep='|')
    df = pd.read_csv(
        'sentiment_analysis/dataset/PPTkoreadrama_preprocessed_final.csv', sep='|')

def load_voice_data():
    global voice  # global variable
    #df = pd.read_csv('dataset/news_dataset_preprocessed_for_django.csv',sep='|')
    voice = pd.read_csv(
        'sentiment_analysis/dataset/drama_voice.csv', sep='|')

# call load data function when starting server
load_df_data()
load_voice_data()


def api_get_sentiment(request):

    drama_list = [
        ['Mouse窺探', 'Mouse窺探|Mouse|mouse'], ['怪物', '怪物'], ['Law School', 'Law|School|law|school'], ['Undercover', 'Under|cover'], ['Run On奔向愛情', 'Run|On|奔向愛情'], ['女神降臨', '女神降臨'], ['五月的青春', '五月的青春'], ['前輩，那支口紅不要塗', '前輩，那支口紅不要塗|前輩那支口紅不要塗'], ['婚詞離曲', '婚詞離曲'], ['所以我和黑粉結婚了', '所以我和黑粉結婚了'], ['黑道律師文森佐', '黑道律師|文森佐'], ['模範計程車', '模範計程車'], ['上流戰爭', 'Penthouse|上流戰爭|penthouse'], ['我的上流世界', '上流世界|Mine'], ['如蝶翩翩', '如蝶翩翩'], ['我是遺物整理師', '我是遺物整理師|Move to Heaven'], ['大發不動產', '大發不動產'], ['黑洞', '黑洞'], ['在我筆下的命運', '在我筆下的命運'], ['某一天滅亡來到我家門前', '某一天滅亡來到我家門前|滅亡']]

    cate = request.GET['cate']

    for i in range(len(drama_list)):
        if cate == drama_list[i][0]:
            df_query = df[df['title'].str.contains(drama_list[i][1])]
    # global variable
    # global  df_query

    # Proceed filtering
    #df_query = df[df['title'].str.contains(cate)]

    sentiCount, sentiPercnt = get_article_sentiment(df_query)

    #data_pos, data_neg = get_key_time_based_sentiment( df_query, freq_type )

    response = {
        'sentiCount': sentiCount,
    }
    return JsonResponse(response)


def api_get_voice(request):
    # getLineChartData
    cate = request.GET['cate']

    '''
    {
        "year": "2021-01-01",
        "value": 0
    }
    '''

        
    # js = js_voice.to_json(orient = 'columns')
    js_voice =[] 
    for i in range(len(voice)):
        if voice.drama[i]==cate:
            js_voice.append({"year":"2021/" + voice.date[i],"value":str(voice.voice[i])})
    # js = json.dumps(js_voice)
    response = {
        'cate': cate,
        'lineChartData': js_voice,
    }
    return JsonResponse(response)


def get_article_sentiment(df_query):
    sentiCount = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    sentiPercnt = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    numberOfArticle = len(df_query)
    for senti in df_query.sentiment:
        # determine sentimental polarity
        if float(senti) >= 0.75:
            sentiCount['Positive'] += 1
        elif float(senti) <= 0.4:
            sentiCount['Negative'] += 1
        else:
            sentiCount['Neutral'] += 1
    for polar in sentiCount:
        sentiPercnt[polar] = int(sentiCount[polar]/numberOfArticle*100)
        # sentiPercnt[polar]=round(sentiCount[polar]/numberOfArticle,2)
    return sentiCount, sentiPercnt
