import re
custlist=[{'name':'kim','gender':'M',"email":'test01@email.com',"birthyear":'2000'},
          {'name':'park','gender':'M',"email":'test02@email.com',"birthyear":'2000'},
          {'name':'hwang','gender':'M',"email":'test03@email.com',"birthyear":'2000'},
          {'name':'lee','gender':'M',"email":'test04@email.com',"birthyear":'2000'}]
page=-1

er = input("""성별을 입력해주세요.\n성별은 M,F,m,f 만 입력가능합니다.""").upper()
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')  
    # 대문자로 변경
    choice = choice.upper()
    print(choice)
    if choice=="I":        
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
                for i in custlist:
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
            custlist.append(customer)
            print(custlist)
            page = len(custlist) - 1
            break

    elif choice=="C":
        print("현재 고객 정보 조회")
    elif choice == 'P':
        print("이전 고객 정보 조회")
    elif choice == 'N':
        print("다음 고객 정보 조회")
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print("메뉴 선택을 잘못하셨습니다. 다시 선택해 주세요.")
