import json

phone_book = {}
phone_book["trump"] = "0912111111"
phone_book["lisa"] = "0922222222"
phone_book["mike"] = "0932333333"
phone_book["energency"] = "119"

with open("phone_book.json", 'w') as f: ##把dict存成json檔
  json.dump(phone_book, f, indent= 4)

name = str(input("請輸入名字"))
if name in phone_book:
    print(f"{name} 的電話是{phone_book[name]}")
else:
    print("電話簿裡沒有這個名字")
    ans = str(input("是否要增加名字進電話簿(yes/no)"))
    if ans == "yes":
        new_number = str(input("請輸入電話號碼："))
        phone_book[name] = new_number
    else:
        print("謝謝你的查詢。")

