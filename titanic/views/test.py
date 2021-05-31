from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Test(object):

    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, fname):
        service = self.service
        self.dataset.context = './data/'
        self.dataset.fname = fname
        self.entity = service.new_model(fname)
    def plot(self):
        this = self.entity
        print(f'Train 의 type 은 {type(this)} 이다.')
        print(f'Train 의 column 은 {this.columns} 이다.')
        print(f'Train 의 상위 5개 데이터는 {this.head()} 이다.')
        print(f'Train 의 상위 5개 데이터는 {this.tail()} 이다.')
