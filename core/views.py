from django.views.generic import TemplateView
from django.shortcuts import render
import requests
from django.template import loader
from django.http import HttpResponse
import json
import random


class PageView(TemplateView):
	template_name = 'page-1.html'

class PageOneView(TemplateView):
	template_name = 'page-1.html'

class PageTwoView(TemplateView):
	template_name = 'page-2.html'
	def get_context_data(self, *args, **kwargs):
		context = super(PageTwoView, self).get_context_data(*args, **kwargs)
		context['name'] = ''
		context['id'] = '1'
		return context






def MatchLive(request):
    url = "https://flashscore.p.rapidapi.com/v1/events/live-list"

    querystring = {"sport_id": "1", "timezone": "-4", "locale": "en_GB"}

    headers = {
        'X-RapidAPI-Key': "c203beaed3mshdee6ff27c9b3eabp1dd3aejsn60d50c3838fa",
        "X-RapidAPI-Host": "flashscore.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    tablehome = []
    tableaway = []
    thomescore=[]
    timageshome=[]
    timagesaway=[]
    turniejtab=[]
    krajtab = []
    randomkey=[]


    datalength = len(response.json()['DATA'])

    for j in range(0, datalength):
     eventslength = len(response.json()['DATA'][j]['EVENTS'])
     for i in range(0, 1):
                gamerand = random.randint(1, 7659898)
                druzyna1 = response.json()['DATA'][j]['EVENTS'][i]['HOME_NAME']
                druzyna2 = response.json()['DATA'][j]['EVENTS'][i]['AWAY_NAME']
                homescore= response.json()['DATA'][j]['EVENTS'][i]['HOME_SCORE_CURRENT']
                awayscore =response.json()['DATA'][j]['EVENTS'][i]['AWAY_SCORE_CURRENT']
                imageshome=response.json()['DATA'][j]['EVENTS'][i]['HOME_IMAGES'][0]
                imagesaway = response.json()['DATA'][j]['EVENTS'][i]['AWAY_IMAGES'][0]
                turniej=response.json()['DATA'][j]['NAME']
                kraj=response.json()['DATA'][j]['COUNTRY_NAME']

                x = druzyna1.split(" ")

                tablehome.append(x[0])
                y = druzyna2.split(" ")
                tableaway.append(y[0])
                timageshome.append(imageshome)
                timagesaway.append(imagesaway)
                tableaway.append(druzyna2)
                turniejtab.append(turniej)
                thomescore.append(homescore+"-"+awayscore)
                krajtab.append(kraj)
                randomkey.append(gamerand)

    zipped = zip(tablehome, timageshome)
    zipped2 = zip(tableaway, timagesaway)
    zipped3 = zip(thomescore, randomkey, turniejtab, krajtab)
    result_dict = {
        "cookie": True
    }
    if request.COOKIES.get('acceptCookies') == '1':
        result_dict = {
            "cookie": False
        }

    if request.COOKIES.get('lang')=='en':
            return render(request, 'pageen.html',
                          {'range': range(1, len(tablehome)), 'tablehome': tablehome, 'tableaway': tableaway,
                           'thomescore': thomescore, 'timageshome': timageshome,
                           'zipped': zipped, 'zipped2': zipped2, 'zipped3': zipped3})
    else:
            return render(request, 'page.html',
                          {'range': range(1, len(tablehome)), 'tablehome': tablehome, 'tableaway': tableaway,
                           'thomescore': thomescore, 'timageshome': timageshome,
                           'zipped': zipped, 'zipped2': zipped2, 'zipped3': zipped3})



def Random(request):
    gamerand=random.choice((7659860,7659864,7659861,765986,7659866,7659868,7659863,7659878,7659886,7659882,7659875,7659876,7659899,
                           7659877,7659872 ,7659874 ,7659870 ,7659880 ,7659898,7659883  ,7659881,7659884 ,7659888,7659867, 7659859,7659865   ))
    url1 = "https://viperscore.p.rapidapi.com/game/"

    querystring1 = {"gameId":gamerand }

    headers1 = {
        'X-RapidAPI-Key': "c203beaed3mshdee6ff27c9b3eabp1dd3aejsn60d50c3838fa",
        "X-RapidAPI-Host": "viperscore.p.rapidapi.com"
    }

    response1 = requests.request("GET", url1, headers=headers1, params=querystring1)
    mecz=response1.json()["slug"].upper()
    wynik = response1.json()["scoreHomeAwaySlug"]

    url = "https://viperscore.p.rapidapi.com/game/lineup"

    querystring = {"gameId": gamerand}

    headers = {
        'X-RapidAPI-Key': "c203beaed3mshdee6ff27c9b3eabp1dd3aejsn60d50c3838fa",
        "X-RapidAPI-Host": "viperscore.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)







    numberteam3 = random.randint(0, 1)
    if(numberteam3==1):
     tt="homeLineup"
     tt2="1"
     player1 = response.json()[tt][0]['name'].split(" ")
     player1 = player1[len(player1) - 1]
     player2 = response.json()[tt][1]['name'].split(" ")
     player2 = player2[len(player2) - 1]
     player3 = response.json()[tt][2]['name'].split(" ")
     player3 = player3[len(player3) - 1]
     player4 = response.json()[tt][3]['name'].split(" ")
     player4 = player4[len(player4) - 1]
     player5 = response.json()[tt][4]['name'].split(" ")
     player5 = player5[len(player5) - 1]
     player6 = response.json()[tt][5]['name'].split(" ")
     player6 = player6[len(player6) - 1]
     player7 = response.json()[tt][6]['name'].split(" ")
     player7 = player7[len(player7) - 1]
     player8 = response.json()[tt][7]['name'].split(" ")
     player8 = player8[len(player8) - 1]
     player9 = response.json()[tt][8]['name'].split(" ")
     player9 = player9[len(player9) - 1]
     player10 = response.json()[tt][9]['name'].split(" ")
     player10 = player10[len(player10) - 1]
     player11 = response.json()[tt][10]['name'].split(" ")
     player11 = player11[len(player11) - 1]

    else:
        tt = "awayLineup"
        tt2 = "2"
        player1 = response.json()[tt][0]['name'].split(" ")
        player1 = player1[len(player1)-1]
        player2 = response.json()[tt][1]['name'].split(" ")
        player2 = player2[len(player2)-1]
        player3 = response.json()[tt][2]['name'].split(" ")
        player3 = player3[len(player3)-1]
        player4 = response.json()[tt][3]['name'].split(" ")
        player4 = player4[len(player4)-1]
        player5 = response.json()[tt][4]['name'].split(" ")
        player5 = player5[len(player5)-1]
        player6 = response.json()[tt][5]['name'].split(" ")
        player6 = player6[len(player6)-1]
        player7 = response.json()[tt][6]['name'].split(" ")
        player7 = player7[len(player7)-1]
        player8 = response.json()[tt][7]['name'].split(" ")
        player8 = player8[len(player8)-1]
        player9 = response.json()[tt][8]['name'].split(" ")
        player9 = player9[len(player9)-1]
        player10 = response.json()[tt][9]['name'].split(" ")
        player10 = player10[len(player10)-1]
        player11 = response.json()[tt][10]['name'].split(" ")
        player11 = player11[len(player11)-1]
    result_dict = {
      "cookie": True
    }
    if request.COOKIES.get('acceptCookies') == '1':
     result_dict = {
        "cookie": False
    }

    if request.COOKIES.get('lang') != 'en':
        return render(request, 'page-1.html',
                      {'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4,
                       'player5': player5, 'player6': player6, 'player7': player7,
                       'player8': player8, 'player9': player9, 'player10': player10, 'player11': player11, 'mecz': mecz,
                       'wynik': wynik, 'tt2': tt2})
    else:
        return render(request, 'page-1en.html',
                      {'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4,
                       'player5': player5, 'player6': player6, 'player7': player7,
                       'player8': player8, 'player9': player9, 'player10': player10, 'player11': player11, 'mecz': mecz,
                       'wynik': wynik, 'tt2': tt2})










def info(request):
    result_dict={
        "cookie" : True
    }
    if request.COOKIES.get('acceptCookies')=='1':
        result_dict = {
            "cookie": False
        }

    if request.COOKIES.get('lang') == 'en':
     return render(request, 'page-2en.html')
    else:
     return render(request, 'page-2.html')






