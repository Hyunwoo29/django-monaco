import pandas as pd
class Conversion(object):

    @staticmethod
    def create_tuple() -> ():
        return (1,2,3,4,5,6,7,8,9)

    @staticmethod
    def convert_list(tp) -> []:
        return list(tp)

    @staticmethod
    def convert_float(ls) -> []:
        return [float(i) for i in ls]

    @staticmethod
    def convert_int(ls) -> []:
        return [int(i) for i in ls]
    @staticmethod
    def list_convert(ls) -> {}:
        return dict(ls)
    @staticmethod
    def str_convert(st) -> ():
        return tuple(list(st))
    @staticmethod
    def hello_to_ls(tp) -> []:
        return list(tp)
    #딕셔너리를 데이터 프레임으로 전환하시오.
    @staticmethod
    def str_tuple(dt) ->{}
        pass




    @staticmethod
    def main():
        c = Conversion()
        i = 0
        f = 0.0
        s = ''
        ls = []
        t = ()
        d = {}
        f_ls = []
        int_ls = []


        while 1:
            m = int(input('0.exit 1.생성 2.리스트전환 3.hello튜플전환 4.튜플->리스트 5.튜플 6.딕셔너리'))
            if m == 0:
                break
            #1부터 10까지 요소를 가진 튜플을 생성하시오.
            elif m == 1:
                tp = c.create_tuple()
                print(tp)
            #1번 튜플을 리스트로 전환하시오.
            elif m == 2:
                ls = c.convert_list(tp)
                print(ls)
            #2번 리스트를 실수(float) 리스트로 전환하시오.
            elif m == 3:
                ls = c.convert_float(ls)
                print(ls)
            #3번 실수(float) 리스트를, 정수 리스트로 전환하시오.
            elif m == 4:
                print(c.convert_int())
            #4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == 4:
                pass
            #'hello'을 튜플로 전환하시오.
            elif m == 4:
                pass
            #6번 튜플을 리스트로 전환하시오.
            elif m == 4:
                pass
            else:
                continue
Conversion.main()
