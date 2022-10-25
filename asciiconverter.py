def ascii_converter():
    print("Welcome To ASCII Convertor".center(47, "_"))
    print('\n')
    user = input("What Do You Want To Convert: ")
    print("_"*45)
    for char in user:
        print(ord((char)), end=" ")


ascii_converter()
