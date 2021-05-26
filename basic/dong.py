# ********************
# -----Data Type------
# ********************

"""
Python has Five standard types
Numbers: int, float, complex
String: str
Collection: list, Tuple, Dictionary, set
"""
"""
ls = ['abcd', 786, 2.42, 'join', 80.5]
tinylist = [123, 'join']
#Create: ls 에 '100'을 추가 Create
ls.append(100)

#Read: ls 의 목록을 출력
print(ls)

#Update: ls와 tynylist 의 결합
ls.extend(tinylist)
print(ls)

#Delete: ls 에서 786을 제거
ls.remove(786)
print(ls)
"""
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')

tp = tp + (100,)
print(tp)

tp1 = tp+tinytp
print(tp1)
# Delete: tp 에서 786을 제거
ls = list(tp)
ls.remove(786)
tp = tuple(ls)
print(tp)



dt = {'abcd': 786, 'john': 70.2}
tinydt = {'홍':'30세'}

dt['tom'] = 100
print(dt)


dt.update(tinydt)
print(dt)


del dt['abcd']
print(dt)