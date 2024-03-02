import requests, urllib.request, json
from django.conf import settings

class RankApi:
    def __init__(self):
        self.api_key = settings.SECRET_KEY
        self.naver_id = settings.NAVER_ID
        self.naver_secret = settings.NAVER_SECRET
    
    def get_day_ranks(self, date):
        response = requests.get("http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key="
                                + self.api_key + "&targetDt=" + date)
        return response.json()['boxOfficeResult']['dailyBoxOfficeList']
 
    def get_weekly_ranks(self, date):
        response = requests.get("http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key="
                                + self.api_key + "&targetDt=" + date + "&weekGb=0")
        return response.json()['boxOfficeResult']['weeklyBoxOfficeList']
    
    def get_naver_movie_api(self, movie_name):
        request = urllib.request.Request("https://openapi.naver.com/v1/search/image?query=" + urllib.parse.quote(movie_name) + "&display=1")
        request.add_header("X-Naver-Client-Id", self.naver_id)
        request.add_header("X-Naver-Client-Secret", self.naver_secret)
        response = urllib.request.urlopen(request)

        if(response.getcode() == 200):
            response_body = response.read()
            response_json = json.loads(response_body.decode('utf-8'))
            return response_json['items'][0]['thumbnail']