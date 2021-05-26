"""회원가입 로그인 마이페이지 내정보수정 회원탈퇴
회원가입 :이메일 아이디 비밀번호"""

class Member(object):

    id = ''
    email = ''
    password = ''
    id1 = ''
    password1 = ''
    def join(self, id,password):
        self.id = f'{id}'
        self.email = f'{password}'
    def login(self,id1,password1):
        self.id1 = f'{id1}'
        self.password1 = f'{password1}'
    def mypage(self, ls):
        pass
    def update(self):
        pass
    def remove(self):
        pass

    @staticmethod
    def main():
        member = Member()
        while 1:
            m = int(input('0.Exit 1.회원가입 2. 로그인 3.마이페이지 4.내정보수정 5.회원탈퇴'))
            if m == 0:
                break
            elif m == 1:
                member.id = input('아이디:')
                member.email = input('이메일:')
                member.password = input('비밀번호:')

            elif m == 2:
                member.id1 = input('아이디:')
                member.password1 = input('비밀번호:')
                if member.id == member.id1 and member.password == member.password1:
                    print("환영합니다.")
                else:
                    print("틀렸습니다.")
            elif m == 3:
                member.mypage()
            elif m == 4:
                member.update()
            elif m == 5:
                id = ''
                email = ''
                password = ''
                member.remove()
            else:
                print("wrong number")
                continue
Member.main()
