import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from parsed_data.models import BlogData


#parser.py
#검색어 입력 키워드
article = str("코로나")

def parse_blog():
    # 최근기사 불러오는 url
    req = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query="+article)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # 태그 a의 title을 불러온다.
    news_titles = soup.select('.list_news li div.news_wrap.api_ani_send div.news_area a[title]')
    data= {}

    for title in news_titles:
        # a의 주소를 불러온다.
        data[title.text] = title.get('href')
    return data

    # 데이터를 json으로 저장하는 방법
    # with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    # json.dump(data, json_file)

# 파이썬 상에서 BlogData 모델의 저장하는 방식
if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()


