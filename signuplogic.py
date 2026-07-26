import json
import random
file = open("storage.json","r")
json_file = json.load(file)
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
        exit()
    print(" ")
    for user in json_file:
        if user["username"]==usern:
            pasw=user["password"]
            break
    passw = input("Enter password: ").strip()
    print(" ")
    file = open("storage.json","r")
    json_file = json.load(file)
    found1=False
    for user in json_file:
        if user["username"] == usern and int(user["password"]) == int(passw):
            print("Login successful!!.....")
            found1=True
            break
    if not found1:
        print("Incorrect password!!.....")
        exit()
else:
    print("Invalid input!")