print("Welcome to the secret Application!")
print("Please log in using your details, ensuring that no CAPITAL letters are used!")
Login = input("Username: ")
Pass = input("Password: ")

if Login == "admin" and Pass == "1234":
    print("Access Granted")
else:
    print("Access Denied")