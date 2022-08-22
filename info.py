import re
while True :
    name = input("What is your name: ").capitalize()#Asking your name  
    if any(char.isdigit() for char in name):  
        print("Please do not include digits in your name.")
        continue #making sure the user writes words
    while True:  
        number = input("What is your number: ")#Asking The user for his number
        if len(number) < 3 :
          print("Number has to be more than 3 Charecters and if you have wrriten words please write numbers")
          continue
        elif type(number) == number.isalpha():
            print("You Have To Write A number")
            break      
        else:
         try:
           number = int(number)
           break  
         except ValueError:
            print(" you have to write a number")#Making Sure The User Writes Integers
    while True :
          city = input("what is your city: ")#Asking The User For His Email
          if any(char.isdigit() for char in city):  
           print("Please do not include digits in your name.") 
           continue
          else:
              break
    while True :
        email1 = input("What is your email:")#asking the user the email
        my_string = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]",email1)#checking if the email is an email or not
        if my_string:   
             print(f"This is your name: {name}")
             print(f"This is your number: {number}")
             print(f"this is your email: {email1}")
             print(f"This is your city: {city}")
             confirm= input("please confirm y or n: ")#asking you to confirm
             if confirm == 'y' or confirm== 'Y':#you either choose y or Y 
                print(confirm)
                quit()
             elif confirm == 'n' or confirm == 'N':#or you choose n or N  
                 break  
             else:
                 print("write yes or no")
                 break
        else:
         continue