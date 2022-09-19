History = [] #Where The History Will Be Stored


def history():#The Function To Store The Code

    Ques = input("Do You Want To See History [Y/N]: ")
    if Ques == "Y" or Ques == "y":
        print(History)
    else:
        quit()



def Calc():#The Calculator Itself
    while True:#Infinte Loop

        Fnumber = input("First Number: ") #Asking The User The First Number
        
        Operation = input("Operation (+ or - or * or /) :  ")# Asking The User The Operation
        
        Snumber = input("Second Number: ")#Asking The User The Second Number

        if Operation == '+':
            P = int(Fnumber) + int(Snumber) #Get`s The Sum Of The Number That The User Entered
            print(P)#Prints The Value
            qui = input("Do You Want To Quit [Y/N] or do yo want to see history [H]: ") #Asking The User Does He Want To Quit Or Does He Want To See The History
            x = f"{str(Fnumber)} {Operation} {str(Snumber)} = {P}" #How The Question And Value Will Be Stored
            History.append(str(x))#Adding The The Question And The Value
            if qui == "Y" or qui == "y":
                break
            elif qui == "N" or qui == "n":
                continue

            elif qui == "H" or qui == "h":
                history()    
       
        
        
        elif Operation == '-':
               M =  int(Fnumber) - int(Snumber)
               y = print(M)
               x = f"{str(Fnumber)} {Operation} {str(Snumber)} = {str(y)}"
               History.append(str(x))
               qui = input("Do You Want To Quit [Y/N] or do yo want to see history [H]:  ")        
               if qui == "Y" or qui == "y":
                break
               elif qui == "N" or qui == "n":
                continue
               elif qui == "H" or qui == "h":
                 history()    
        
        
        elif Operation == '/':
                D = int(Fnumber) / int(Snumber)
                g = print(D)
                x = f"{str(Fnumber)} {Operation} {str(Snumber)} = {str(g)}"
                History.append(str(x))
                qui = input("Do You Want To Quit [Y/N] or do yo want to see history [H]:  ")   
                if qui == "Y" or qui == "y":
                 quit()
                elif qui == "N" or qui == "n":
                    continue
                elif qui == "H" or qui == "h":
                 history()    
        
        elif Operation == '*':
               T=  int(Fnumber) - int(Snumber)      
               l = print(T)
               x = f"{str(Fnumber)} {Operation} {str(Snumber)} = {str(l)}"
               History.append(str(T))
               qui = input("Do You Want To Quit [Y/N] or do yo want to see history [H]:  ")   
               if qui == "Y" or qui == "y":
                 break
               elif qui == "N" or qui == "n":
                    continue
               elif qui == "H" or qui == "h":
                 history()    
Calc()                 
history()

