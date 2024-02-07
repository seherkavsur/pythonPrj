#Autherization program

def initializePage():
    print("Welcome to Web Site...")
    return True

def insertUserName():
    print("Please enter your username:")
    name = input()

    if name:
         print("ok")
    else:
         print("name is empty!!!")     
         return False

    if name == "seherkavsur":
        return True
    elif name == "seher":
         return True
    else:
        print("password is not correct")
        return False
    
def insertPassword():
        print("Please enter your password")
        password = input()
        if password == "1234":
            print("Success")
            return True
        else:
            print("check your password")
            return False

result = initializePage()
if result == True:
    res = insertUserName()
    if res == True:
         res2 = insertPassword()
         if res2 == True:
              print("Welcome to your page!!")  
         else:
              print("please try again!")     