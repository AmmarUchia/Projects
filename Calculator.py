def calc():
    while True:    
     first_Number = input("Enter First Number: ")
     Second_Number = input("Enter Second Number: ")
     operator = input("What is The Operator That You Want + or - or / or * = ")
     if operator == '+':
        print(int(first_Number) + int(Second_Number))
        ask = input("Do You Want To Quit Y/N : ")
        if ask == 'y'or ask == 'Y':
          break 
        elif ask == 'N' or ask == 'n':
            continue
     elif operator == '-':
        print(int(first_Number) - int(Second_Number))
        ask = input("Do You Want To Quit Y/N : ")
        if ask == 'y' or ask == 'Y':
          break
        elif ask == 'N'or ask == 'n':
            continue
     elif operator == '/':
        print(int(first_Number) / int(Second_Number))
        ask = input("Do You Want To Quit Y/N : ")
        if ask == 'y'or ask == 'Y':
          break
        elif ask == 'N'or ask == 'n':
            continue
     elif operator == '*':
        print(int(first_Number) * int(Second_Number))
        ask = input("Do You Want To Quit Y/N : ")
        if ask == 'y'or ask == 'Y':
          break
        elif ask == 'N'or ask == 'n':
            continue
calc()        