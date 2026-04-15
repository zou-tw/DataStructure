def register() :
    account = input()
    if account in user_data :
        print("帳號已存在")
    else :
        password = input()
        user_data[account] = password
        print("註冊成功")
def log_in() :
    account = input()
    if account not in user_data :
        print("帳號輸入錯誤")
    else :
        password = input()
        if password == user_data[account] :
            print("登入成功")
        else :
            print("密碼輸入錯誤")
user_data = dict()
while True :
    option = input("請選擇操作選項(a.註冊 b.登入 c.退出)")
    if option not in "abc" :
        print("選項錯誤，請重新輸入選項")
    else :
        if option == 'a' :
            register()
        elif option == 'b' :
            log_in()
        else :
            break
