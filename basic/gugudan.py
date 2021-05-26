"""
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1~9의 곱을 출력하는 어플이다.
단, 단은 정수이다. = 0
ex 단은 싫수다 = 0.0
"""
class Gugudan(object):
    dan = 0
    dict = {}

    def print_selected_dan(self):
        for i in range(1,10):
            print(f'{self.dan} x {i} = {self.dan * i}')

    def print_all_dan(self):
        for i in range(1, 10):
            for j in range(1,10):
                print(f'{i} x {j} = {i*j}')
    def print_dict_dan(self):
        d = self.dict
        for i in range(1, 10):
            d[i] = self.dan * i
        print('딕셔너리 출력')
        print(self.dict)
        for k in d.keys():
            print(f'{self.dan} * {k} = {d.get(k)}')

    @staticmethod
    def main():
        d = Gugudan()
        while 1:
            m = int(input('0.exit 1.Insert input 2.all dan 3.input dan with dict'))
            if m == 0:
                break
            elif m == 1:
                d.dan=int(input("단을 입력하시오:"))
                d.print_selected_dan()
            elif m == 2:
                d.print_all_dan()
            elif m == 3:
                d.dan = int(input('단 입력'))
                d.print_dict_dan()


            else:
                print("worng number")
                continue

Gugudan.main()
