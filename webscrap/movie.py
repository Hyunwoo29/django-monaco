from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup


class Movie(object):
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    class_name= ''
    title_ls = []
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    get_ranking = []
    dict = {}
    count = []
    df = None

    def scrap(self):

        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div',{"class":self.class_name})
        for i in all_div:
            print(f'{i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        for i in range(len(self.title_ls)):
            self.count.append(i+1)

        driver.close()

    def title_dict(self):
        for i, j in enumerate(self.count):
            self.dict[j] = self.title_ls[i]
        print(self.dict)

    def dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')

    def to_csv(self):
        path = './data/movie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


if __name__ == '__main__':
    naver = Movie()
    naver.class_name = 'tit3'
    naver.scrap()
    naver.title_dict()
    naver.dataframe()
    naver.to_csv()