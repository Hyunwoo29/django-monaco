import pandas as pd
from bs4 import BeautifulSoup
import requests


class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    get_title = []
    get_artist = []
    dict = {}

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls1 = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls1:
            print(f' {i.find("a").text}')
            self.get_title.append(i.find("a").text)
        print('------ 가수 --------')
        ls2 = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls2:
            print(f' {i.find("a").text}')
            self.get_artist.append(i.find("a").text)

    def title_dict(self):
        for i, j in enumerate(self.get_title):
            self.dict[j] = self.get_artist[i]
        print(self.dict)
    def dic_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient = 'index')
        print(self.df)

    def df_to_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0-exit, 1-input time, 2-output 3.dict 4.df변환 5.csv넣기')
            if menu == '0':
                break
            elif menu == '1':
                melon.set_url(input('스크래핑할 날짜 입력'))  # '2021052511'
            elif menu == '2':
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()
            elif menu == '3':
                melon.title_dict()
            elif menu == '4':
                melon.dic_to_dataframe()
            elif menu == '5':
                melon.df_to_csv()
            else:
                print('Wrong number')
                continue

Melon.main()