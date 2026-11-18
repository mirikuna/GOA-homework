iteration = 1

while iteration <= 14:
    print(iteration)
    iteration = iteration + 1




password = 1234

user_password = int(input("შეიყვანეთ პაროლი: "))

while user_password != password:
    print("პაროლი არასწორია!")
    
    user_password = int(input("სცადეთ თავიდან: "))

print("პაროლი სწორია! სისტემა გახსნილია.")