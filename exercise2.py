def valid_email(email):
    x = "@"
    y = "."
    if x in email and y in email:
        return True
    else:
        return False
if(valid_email(input("Enter your email:"))):
    print("Your email is valid.")
else:
    print("Your email is not valid.")



