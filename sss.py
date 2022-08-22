while True :
    name = input("What is your name: ").capitalize()#Asking your name  
    if any(char.isdigit() for char in name):  
        print("Please do not include digits in your name.")
        continue #making sure the user writes words
    while True:  
        number = input("What is your number: ")#Asking The user for his number
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
        email1 = input("what is your email: ")#Asking The User For His Email
        if any(char.isdigit() for char in email1):  
         print("Please do not include digits in your name.")        
         continue #Making Sure The User Writes An Email
        else:
         print(f"This is your name: {name}")
         print(F"This is your number: {number}")
         print(F"this is your email: {email1}")
         print(f"This is your city: {city}")
         quit()
      
        
        
        
