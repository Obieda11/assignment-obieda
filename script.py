print("Welcome to Obieda's Best Cinema World!")
age = int(input("How Old Are You? "))
Bill = 0 

if age <= 12:
    print("your ticket price is 5$ ")
    Bill + 5
elif age >12 and age <18:
    print("your ticket price is 8$ ")  
else:
    print("your ticket price is 10$")

print("Thank you for your visit")