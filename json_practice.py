import json

with open('phone_book.json', 'r') as f: ##讀取phone_book.json
  ## 轉成Python Dict
  phone_book = json.load(fp = f)

print(phone_book)

name = str(input("請輸入名字"))
if name in phone_book:
    print(f"{name} 的電話是{phone_book[name]}")
else:
    print("電話簿裡沒有這個名字")
    ans = str(input("是否要增加名字進電話簿(yes/no)"))
    if ans == "yes":
        new_number = str(input("請輸入電話號碼："))
        phone_book[name] = new_number
        
        with open("phone_book.json", 'w') as f: ##把dict存成json檔
            json.dump(phone_book, f, indent= 4)
    else:
        print("謝謝你的查詢。")