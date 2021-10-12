import urllib
import webbrowser

def login():
    print("\tLogin")
    reguser = str(input("Enter your username: "))
    regpass = str(input("Enter your password: "))
    f = open("sample1.txt", "r")
    f2 = open("sample2.txt", "r")
    readit = f.readlines()
    readit2 = f2.readlines()
    if reguser not in readit and regpass not in readit2:
        print("Username or Password Incorrect!")
        f.close()
        f2.close()
        print("\t\t\t\t\tIt seems like you dont have an account yet, Do you want to create one?")
        gogo = int(input("\t\t\t\t\tEnter 1 if you want to create one and 2 if you already have an account: "))
        if gogo == 1:
            register()
        elif gogo == 2:
            login()
    else:
        if reguser not in readit and regpass not in readit2:
            print("Username or Password Incorrect")
            print("\t\t\t\t\tIt seems like you dont have an account yet, Do you want to create one?")
            gogo = int(input("\t\t\t\t\tEnter 1 if you want to create one and 2 if you already have an account: "))
            if gogo == 1:
                register()
            elif gogo == 2:
                login()
        else:
            print("Logged In Succesful!\n")
            stayin()
            logout()
    


def register():
    print("\tRegister")
    regisuser = str(input("Enter your username: "))
    if len(regisuser) < 8:
        print("Username should be 8-15 character long")
        register()
    regisuser2 = str(input("Confirm your username: "))
    f = open("sample1.txt", "r")
    readit2 = f.read()
    if regisuser == regisuser2:
        f = open("sample1.txt", "a")
        f.write("\n")
        f.write(regisuser)
        f.close()
        f = open("sample1.txt", "r")
        readit2 = f.read()
        if regisuser in readit2:
            regispass = str(input("Enter your password: "))
            if len(regispass) < 4:
                print("Password should be 4 or more characters long")
                register()
            else:
                regispass2 = str(input("Confirm your password: "))
                g = open("sample2.txt", "r")
                readit3 = g.read()
                if regispass == regispass2:
                    g = open("sample2.txt", "a")
                    g.write("\n")
                    g.write(regispass)
                    g.close()
                    g = open("sample2.txt", "r")
                    readit3 = g.read()
                    if regispass in readit3:
                        print("Register Sucess")
                        print("You can now LogIN to your account")
                        login()
                else:
                    print("Password is Wrong")
                    retrypass = int(input("Enter 1 if you want to continue"))
                    if retrypass == 1:
                        register()
                    else:
                        register()
    else:
        print("Username is Wrong")
        retryuser = int(input("Enter 1 if you want to continue: "))
        if retryuser == 1:
            register()
        else:
            register()
 

def startitall():
    f = open("sample1.txt", "r")
    f.close()
    g = open("sample2.txt", "r")
    g.close()
    print("Welcome!\nDo you want to register for an account?")
    choice = int(input("Enter 1 if you have an account or Enter 2 if you want to register: "))
    if choice == 1:
        login()
    elif choice == 2:
        register()
    else:
        startitall()


def logout():
    logout1 = int(input("\t\t\t\t\t\t\tLogout:\n\t\t\t\t\t\t\tEnter 2 to stay, Enter 1 to Logout: "))
    if logout1 == 1:
        print("Successfuly Logged Out")
        relog()
    else:
        stayin()
        logout()
def stayin():
    webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')
    print("Pretend this is the Content")
def relog():
    login()

    
startitall(), login()
    
    




    
