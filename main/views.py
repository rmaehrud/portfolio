from django.shortcuts import render, redirect
from .models import PortfolioList
from .serializers import PortfolioSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from parsed_data.models import BigData
import json
import requests
from bs4 import BeautifulSoup
import urllib.request as reb
from fake_useragent import UserAgent


def index(request):
    portfolio = PortfolioList.objects.all()
    big = BigData.objects.all()

    if request.GET.get('code'):
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome",
            "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }

        try:
            req = session.get(
                "https://www.jecheon.go.kr/site/corona01/index.html",headers=headers)
            html = req.content.decode('utf8')
            soup = BeautifulSoup(html, 'html.parser')
            news_titles = soup.select(
                '#route > div > div:nth-child(5) > table > tbody > tr ')
            title = []
            content = []
            for a in news_titles:
                # a의 주소를 불러온다.)
                data1 = a.get('data-content')
                title.append(data1)
                data2 = a.text
                content.append(data2)

            for name, value in zip(title, content):
                data = {name: value}
                BigData(text=value).save()
            code = request.GET['code']
            url = "https://kauth.kakao.com/oauth/token"  # 토큰을 받기 위한 url 주소

            data = {
                "grant_type": "authorization_code",
                "client_id": "df340b35b08e36a4a7efeb9cdb70ad63",
                "redirect_uri": "http://localhost:8000/index/",
                "code": code
            }  # 데이터
            response = requests.post(url, data=data)  # url과 데이터를 post 요청을 해주었음

            tokens = response.json()  # json 형태로 응답 요청
            for key, value in tokens.items():
                if key == 'access_token':
                    access_token = value
                    # 코로나 정보
                    url1 = 'http://127.0.0.1:8000/parsed_data/bigdata/'

                    # 요청
                    res = reb.urlopen(reb.Request(url1)).read().decode('UTF-8')

                    # 응답 데이터 str -> json 변환 및 data 값 출력
                    restapi_json = json.loads(res)

                    kakao_to_me_uri = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
                    headers = {
                        'Content-Type': "application/x-www-form-urlencoded",
                        'Authorization': "Bearer " + access_token,
                    }

                    # json->str
                    template_json_data = 'template_object=' + \
                                         json.dumps(restapi_json[-1])

                    # link 모델의 기본키를 웹 url 모바일 url로 변경하여 메시지 보내기
                    template_json_data = template_json_data.replace(
                        "12341234",
                        "{\"web_url\": \"https://www.jecheon.go.kr/site/corona01/index.html\", \"mobile_web_url\": \"https://www.jecheon.go.kr/site/corona01/index.html\"}")

                    response = requests.request(
                        method="POST", url=kakao_to_me_uri, data=template_json_data, headers=headers)
                    print(response.json())
                    big.delete()
        except ConnectionAbortedError:
            print("오류")



    context = {
        'portfolio': portfolio,
        'big': big,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


class PortfolioView(viewsets.ModelViewSet):
    queryset = PortfolioList.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
