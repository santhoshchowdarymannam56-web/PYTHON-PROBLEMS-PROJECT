password=input("Enter the password:")

if len(password)<6:
    print("Invalid")
else:
    fifth_char=password[4]

    if not (fifth_char.isdegit()):
        print("Invalid")