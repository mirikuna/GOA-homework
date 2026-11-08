numb_1=int (input("რა არის მართკუთხედის სიგანე?"))
print(numb_1)
numb_2=int (input("რა არის მართკუთხედი სიგრძე?"))
print(numb_1 * numb_2)


number=int(input("რა არის თქვენი რიცხვი?"))
print(number)
if number % 2== 0:
    print("თქვენი რიცხვი ლუწია")
else:
    print("თქვენი რიცხვია კენტი")

age=int(input("რამდენი წილისა ხართ?"))
if age>18:
    print("მოგესალმებით, თქვენ სრულწლოვანი ხართ")
elif age<18:
    print("შესვლა აკრძალულია ბოვშო!")


temperature=int(input("რა ტემპერატურაა ამ წამს?"))
if temperature<0:
    print("ძალიან ცივა ჩაიცვი რამე!")
elif 20>temperature>0:
    print("მშვენიერი ამინდია ჩაინცვი რაც გსურს")
else:
    print("ძალიან ცხელა!")

balance=500
balance_withdraw=int(input("რა თანხის გამოტანა გსურთ?"))
if balance_withdraw>500:
    print("ბალანსზე საკმარისი თანხა არაა!")
elif balance_withdraw<500:
    print(balance - balance_withdraw)

total_price=int(input("რა ღირს თქვენი შენაძენი?"))
if total_price>100:
    print(total_price * 0.8)
elif total_price<100:
    print(total_price * 0.9)
elif total_price<51:
    print(total_price)

correct_password ="miro mgeli"
user_password=input("პაროლი")
if user_password==correct_password:
    print("წვდომა დაშვებულია")
else:
    print("პაროლი არასწორია")

score=int(input("თქვენი ქულა?"))
if 100>score>91:
    print("A")
elif 90>score>81:
    print("B")
elif 80>score>71:
    print("C")
elif 70>score>61:
    print("D")
elif 60>score>51:
    print("E")
elif 51>score:
    print("F!!!")

# total_seconds = input("შეიყვანე წამების რაოდენობა")

# minutes = total_seconds // 60
# seconds = total_seconds % 60
# if total_seconds<3600:
#     print(minutes + seconds)

# if minutes>60:

item_name =str(input("ნივთის სახელი?"))
price= float(input("ნივთის ფასი?"))
quanity=int(input("ნივთის რაოდენობა?"))
total_cost = price * quanity
if total_cost<50:
    has_discount=True
else:
    has_discount=False
print(item_name)
print(price)
print(quanity)
print(total_cost)
print(has_discount)

#boss level!!!!!!!!!!
symbol = input("შეიყვანე სიმბოლო: ")

print("  " + symbol)
print(" " + symbol * 3)
print(symbol * 5)
print(" " + symbol * 3)
print("  " + symbol)
#მარტივი იყო


#boss level N2!!!!!!!!!
secret_number=6
guess_number=int(input("თქვენი რიცხვი?"))
if guess_number<6:
    print("ცოტა მეტი")
elif guess_number ==6:
    print("სწორიაა")
guess_number=int(input("თქვენი მეორე რიცხვი?"))
if guess_number>6:
    print("ცოტა ნაკლები")
elif guess_number ==6:
    print("სწორიაა")