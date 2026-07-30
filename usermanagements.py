import json
import random
file = open("storage.json","r")
json_file = json.load(file)
print("Choose the procedure you want to perform:")
procedure = input("1. Register\n2. Edit user\n3. Delete user\n4. Exit\nYour choice: ").lower()
def login():
    file = open("storage.json","r")
    json_file = json.load(file)
    usern=input("Enter username: ").strip().lower()
    print(" ")
    found=False
    for user in json_file:
        if usern == user["username"]:
            print("Username Found!!.....")
            found=True
            break
    if not found:
        print("Username not found!!.....")
        print("Try Again!..")
        print(" ")
    passw = input("Enter password: ").strip()
    print(" ")
    file = open("storage.json","r")
    json_file = json.load(file)
    found1=False
    for user in json_file:
        if user["username"] == usern and user["password"] == passw:
            print("Login successful!!.....")
            found1=True
            return usern,passw
    if not found1:
        print("Incorrect password!!.....")
        return 1
    file.close()
if procedure == "1" or procedure == "register":
    type = input("Sign up or Login? (signup/login): ").strip().lower()
    print(" ")
    if type == "signup":
        usern = input("Enter username: ").strip().lower()
        print(" ")
        if usern == "":
            print("Username cannot be empty!")
            exit()
        for user in json_file:
            if user["username"]==usern:
                print("Username already exists!")
                exit()
        else:
            print("Suggested password:")
            char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
            pass1=""
            for i in range(8):
                pass1+=random.choice(char)
            print(pass1)
            print(" ")
            passw = input("Enter password: ").strip()
            new_user = {"username": usern, "password": passw}
            json.dumps(new_user, indent=4)
            file.close()
            with open("storage.json","w") as f:
                json_file.append(new_user)
                json.dump(json_file, f, indent=4)
            print("User created successfully!")
    elif type == "login":
        login()
    else:
        print("Invalid input!")
elif procedure == "2" or procedure == "edit user":
    print(" ")
    print("Login to edit user details:")
    file = open("storage.json","r")
    json_file = json.load(file)
    usern=input("Enter username: ").strip().lower()
    print(" ")
    found=False
    for user in json_file:
        if usern == user["username"]:
            print("Username Found!!.....")
            found=True
            break
    if not found:
        print("Username not found!!.....")
        print("Try Again!..")
        print(" ")
        exit()
    passw = input("Enter password: ").strip()
    print(" ")
    file = open("storage.json","r")
    json_file = json.load(file)
    found1=False
    for user in json_file:
        if user["username"] == usern and user["password"] == passw:
            print("Login successful!!.....")
            found1=True
    if not found1:
        print("Incorrect password!!.....")
        exit()
    file.close()
    print(" ")
    print("What do you want to edit?")
    edit_choice = input("1. Username\n2. Password\n3. Exit\nYour choice: ").strip().lower()
    if edit_choice == "1" or edit_choice == "username":
        found2=False
        new_username = input("Enter new username: ").strip().lower()
        for user in json_file:
            if user["username"]==new_username:
                print("Username already exists!")
                found2=True
                print(" ")
                print("Try again!")
                new_username = input("Enter new username: ").strip().lower()
        if not found2:
            print(" ")
            for user in json_file:
                if user["username"]==usern:
                    user["username"]=new_username
                    break
                    with open("storage.json","w") as f:
                        json.dump(json_file, f, indent=4)
                        print("Username updated successfully!")
    elif edit_choice == "2" or edit_choice == "password":
        new_password =input("Enter new password: ").strip()
        for user in json_file:
            if user["username"]==usern:
                user["password"]=new_password
                break
        with open("storage.json","w") as f:
            json.dump(json_file, f, indent=4)
        print("Password updated successfully!")
    elif edit_choice == "3" or edit_choice == "exit":
        print("Exiting...")
        exit()
    else:
        print("Invalid input!")
elif procedure == "3" or procedure == "delete user":
    print(" ")
    print("Login to delete user:")
    file = open("storage.json","r")
    json_file = json.load(file)
    usern=input("Enter username: ").strip().lower()
    print(" ")
    found=False
    for user in json_file:
        if usern == user["username"]:
            print("Username Found!!.....")
            found=True
            break
    if not found:
        print("Username not found!!.....")
        print("Try Again!..")
        print(" ")
    passw = input("Enter password: ").strip()
    print(" ")
    file = open("storage.json","r")
    json_file = json.load(file)
    found1=False
    for user in json_file:
        if user["username"] == usern and user["password"] == passw:
            print("Login successful!!.....")
            found1=True
    if not found1:
        print("Incorrect password!!.....")
    print("  ")
    # Deletion of account
    permission=input("Are you sure? (Yes/No): ").strip().lower()
    if permission == "yes":
        for user in json_file:
            if user["username"]==usern:
                with open("storage.json","w") as File:
                    json_file.remove(user)
                    json.dump(json_file,File,indent = 4)
                    print("Deletion succesfull")
                    file.close()
    elif permission=="no":
        print(" ")
        print("Thank you for the Input!..")
        exit()
    else:
        print("Invalid Input")
elif procedure=="4" or procedure=="exit":
    print("Exiting....")
    exit()
else:
    print("Invalid Inpupt!..")