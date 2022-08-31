import re
condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" 
Email = input("Enter an email : ")
if re.search(condition,Email):
    print("Valid email!")
else:
    print("Invalid email!")