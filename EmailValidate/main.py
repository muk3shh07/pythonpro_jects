import re
email_condition = "^[a-z]+[\\._]?[a-z 0-9] + [@]\w{2,3}$"
user_email = input("Enter your Email::")

#ifconditions
if re.search(email_condition,user_email):
    print("Proceeeed")
else:
    print("Incorrect Email")