import re
custlist=[]
page=-1
# page = 데이터가 몇개 들어가 있는지를 알려주는 역활을 할 것이다.

while True:
    print(page)
    choice=input("""
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    """).upper()

    if choice =="I":
        customer = {"name":"", "sex":"", "email":"", "birthyear":""}
        customer["name"] = input("name = ")

        while True:
            customer["sex"] = input("sex = ")
            customer['sex']=customer['sex'].upper()
            if customer["sex"] in ("F","M"):
                break

        while True: # 정규식으로 이메일 검사하기
            regex = re.compile("^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,5}$")
            # ^[a-z][a-z0-9]{4,10} : 소문자 a~z 까지 첫글자로 시작하는 5개~11개 짜리 ID
            # [a-zA-Z]{2,6} : 대문자든 소문자든 상관없이 최소 2자리~6자리까지 들어올수 있다.
                        
            while True:
            # p = re.compile("[^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$]")
                customer["email"] = input("email = ")
                golbang = regex.search(customer["email"])
                if golbang != None:
                    break
                else:
                    print('"@"를 포함한 정확한 이메일을 써주세요.')
            
            check=0
            for i in custlist:
                if i["email"]==customer["email"]:
                    check=1
            if check==0:
                break
            print("중복되는 이메일이 있습니다.")

        while True:
            customer["birthyear"] = input("birthyear = ")
            if len(customer["birthyear"])==4 and customer["birthyear"].isdigit():
                # 문자열에 있는 값들이 숫자값으로 조합이 되어있는지 알아보는 함수이다.
                break
            
        print(customer)
        custlist.append(customer)
        print(custlist)
        page = len(custlist)-1
        print(page)

    elif choice == "C":
        if page >= 0:
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")        
         
    elif choice == "P":
        if page <= 0:
            print("첫 번 째 페이지이므로, 이전 페이지 이동이 불가합니다.")
            print(page)
        else:
            page -= 1
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(custlist[page])           

    elif choice == "N":
        if page >= len(custlist)-1:
            print("마지막 페이지이므로, 다음 페이지 이동이 불가합니다.")
            print(page)
        else:
            page += 1
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(custlist[page])  

    elif choice == "U": 
        while True:
            check_email = input("수정을 원하는 데이터의 이메일을 입력하세요 : ")
            idx = -1

            for i in range(0,len(custlist)):
                if check_email==custlist[i]["email"]:
                    idk = i

            if idk == -1:
                print("등록되지 않은 이메일입니다.")
                break 

            while True:
                select=int(input('''
                수정을 원하는 정보를 선택
                1. name
                2. sex
                3. birthyear
                4. quit
                선택 : '''))
                if select == 1:
                    custlist[idk]['name']=input("name =")
                    break
                elif select == 2:
                    while True:
                        custlist[idk]["sex"] = input("sex = ")
                        custlist[idk]['sex']=custlist[idk]['sex'].upper()
                        if custlist[idk]["sex"] in ("F","M"):
                            break
                    break
                elif select == 3:
                    while True:
                        custlist[idk]["birthyear"] = input("birthyear = ")
                        if len(custlist[idk]["birthyear"])==4 and custlist[idk]["birthyear"].isdigit():
                            break
                    break
                elif select == 4:
                    break
                else:
                    print("다시입력하시오")            
            break
                  
    elif choice == "D":
        delok=0
        check_email = input("삭제을 원하는 데이터의 이메일을 입력하세요 : ")
        
        for i in range(0,len(custlist)) :
            if check_email == custlist[i]["email"]:
                print("{} 고객님의 정보가 삭제되었습니다.".format(custlist[i]["name"]))
                del custlist[i]
                print(custlist)
                page=len(custlist)-1
                delok=1
                break

        if delok == 0:
            print("등록되지 않은 이메일입니다.") 

    elif choice == "Q":
        print("프로그램 종료")
        break
    else:
        print("잘못 입력 하셨습니다.")