import requests
import json
from django.conf import settings

class RankApi:
    def __init__(self):
        self.api_key = settings.SECRET_KEY
    
    def get_day_rank(self, date):
        response = requests.get("http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key="
                                + self.api_key + "&targetDt=" + date)
        return response.json()['boxOfficeResult']['dailyBoxOfficeList']