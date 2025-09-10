import re
import sys

class Customer:

    def __init__(self):
        self.custlist=[{'name':'kim','gender':'M',"email":'test01@email.com',"birthyear":'2000'},
          {'name':'park','gender':'M',"email":'test02@email.com',"birthyear":'2000'},
          {'name':'hwang','gender':'M',"email":'test03@email.com',"birthyear":'2000'},
          {'name':'lee','gender':'M',"email":'test04@email.com',"birthyear":'2000'}]
        self.page=1
        while True:
            self.exe(self.display())

    def display(self):
        choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 고객 정보 입력
        C - 현재 고객 정보 조회
        P - 이전 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 고객 정보 수정
        D - 고객 정보 삭제
        Q - 프로그램 종료
        ''').upper()
        return choice
    
    def exe(self, choice):
        if choice=="I":
            self.insertData()
        elif choice=="C":
            self.viewCustomer()
        elif choice == 'P':
            self.viewPrevious()
        elif choice == 'N':
            self.viewNext()
        elif choice=='D':
            print("고객 정보 삭제")
            self.deleteData()
        elif choice=="U": 
            print("고객 정보 수정")
        elif choice=="Q":
            print("프로그램 종료")
            sys.exit()
        else:
            print("메뉴 선택을 잘못하셨습니다. 다시 선택해 주세요.")
    
    def insertData(self):
        print("고객 정보 입력")
        customer={'name':'','gender':'',"email":'',"birthyear":''}
        while(True):
            while(True):
                name = input("이름을 입력해주세요.")
                if (name.isalpha()):
                    customer[name] = name
                    break
                else:
                    print("이름은 문자로만 입력해주세요.")
            
            while(True):
                gender = input("""성별을 입력해주세요.\n성별은 M,F,m,f 만 입력가능합니다.""").upper()
                if gender == "M" or gender == "F":
                    customer[gender] = gender
                    break
                else:
                    print("성별은 M,F,m,f 만 입력 가능합니다.")
            email_pattern = re.compile(r'^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            while(True):
                email = input("이메일을 입력해주세요.")
                check = 0
                for i in self.custlist:
                    if i["email"] == email:
                        print("이미 있는 이메일 입니다.")
                        check = 1
                        break

                if check == 0:
                    
                    if email_pattern.match(email):
                        customer[email] = email
                        break
                    else:
                        print("이메일 형식 example@email.com")
            
            while(True):
                customer["birthyear"] = input("출생년도 4자리를 입력해주세요.")
                if str(customer["birthyear"].isdigit()) and len(customer["birthyear"]) == 4:
                    customer["birthyear"] = int(customer["birthyear"])
                    break
                else:
                    print("출생년도는 숫자 4자리를 입력해주세요.")
            print(customer)
            self.custlist.append(customer)
            print(self.custlist)
            page = len(self.custlist) - 1
        
    def viewCustomer(self):
        print("현재 고객 정보 조회")
        if self.page >= 0:
            print("현재 페이지는 {} 입니다.".format(self.page+1))
            print(self.custlist[self.page])
        else:
            print("입력된 정보가 없습니다.")

    def viewPrevious(self):
        print("이전 고객 정보 조회")
        if self.page <= 0:
            print("현재 첫번째 페이지 이므로 이동할 수 없습니다.")
        else:
            self.page -= 1
            print("현재 페이지는 {} 입니다.".format(self.page+1))
            print(self.custlist[self.page])
        
    def viewNext(self):
        print("다음 고객 정보 조회")
        if self.page >= len(self.custlist) - 1:
            print("현재 마지막 페이지 이므로 이동할 수 없습니다.")

        else:
            self.page += 1
            print("현재 페이지는 {} 입니다.".format(self.page+1))
            print(self.custlist[self.page])


    def deleteData(self):
        choice = input("삭제하고 싶은 고객 email을 입력하시오.")
        delok = 0
        for i in range(0, len(self.custlist)):
            while self.custlist[i]['email'] == choice:
                print("{} 고객님의 정보가 삭제되었습니다.".format(self.custlist[i]['name']))
                del self.custlist[i]
                self.page = len(self.custlist) - 1
                delok = -1
                break
            
            if delok == -1:
                break

    def updateData(self):
        choice = input("수정하고 싶은 고객의 email을 입력하시오.")
        upok = 0
        for i in range(0, len(self.custlist)):
            while self.custlist[i]['email'] == choice:
                self.custlist[i]['name'] = input("이름을 입력해주세요 >>>")
                self.custlist[i]['gender'] = input("성별을 입력 >>>")
                self.custlist[i]['birthyear'] = input('생일 입력 >>>')
                

if __name__ == '__main__':
    Customer()