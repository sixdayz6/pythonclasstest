import re

def insertData(custlist, page):
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
        return page
    
def viewCustomer(custlist, page):
    print("현재 고객 정보 조회")
    if page >= 0:
        print("현재 페이지는 {} 입니다.".format(page+1))
        print(custlist[page])
    else:
        print("입력된 정보가 없습니다.")

def viewPrevious(custlist, page):
    print("이전 고객 정보 조회")
    if page <= 0:
        print("현재 첫번째 페이지 이므로 이동할 수 없습니다.")
        return page
    else:
        page -= 1
        print("현재 페이지는 {} 입니다.".format(page+1))
        print(custlist[page])
        return page
    
def viewNext(custlist, page):
    print("다음 고객 정보 조회")
    if page >= len(custlist) - 1:
        print("현재 마지막 페이지 이므로 이동할 수 없습니다.")
        return page
    else:
        page += 1
        print("현재 페이지는 {} 입니다.".format(page+1))
        print(custlist[page])
        return page

def deleteData(custlist, page):
    choice = input("삭제하고 싶은 고객 email을 입력하시오.")
    delok = 0
    for i in range(0, len(custlist)):
        while custlist[i]['email'] == choice:
            print("{} 고객님의 정보가 삭제되었습니다.".format(custlist[i]['name']))
            del custlist[i]
            page = len(custlist) - 1
            delok = -1
            break
        
        if delok == -1:
            break
    return page

def updateData(custlist, page):
    choice = input("수정하고 싶은 고객의 email을 입력하시오.")
    upok = 0
    for i in range(0, len(custlist)):
        while custlist[i]['email'] == choice:
            custlist[i]['name'] = input("이름을 입력해주세요 >>>")
            custlist[i]['gender'] = input("성별을 입력 >>>")
            custlist[i]['birthyear'] = input('생일 입력 >>>')
            

