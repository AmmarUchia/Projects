# asking the user for the input
text = input("Enter The Text Here ==> ")

# Defining a function


def binconverter():
    storage = 0
    amount_of_times = 1

    # Getting The Binary Value

    result = [bin(ord(letter)) for letter in text]
    while storage < len(result):
        if result == '0b100000':
            print("Hello There")
        print(f"{amount_of_times} letter ==> {result[storage]}")
        amount_of_times += 1


binconverter()
