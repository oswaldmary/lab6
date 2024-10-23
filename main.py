#encode function
def encode(user_password):
    encoded_user_password = ""
    for i in range (0, len(user_password)):
        new_int = ((int(user_password[i])) + 3)
        if new_int >=10:
            new_int = new_int - 10
        encoded_user_password = encoded_user_password + str(new_int)
    return encoded_user_password






#main function
if __name__ == '__main__':
    #loop menu
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            user_password = input("Please enter your password to encode: ")
            encoded_user_password = encode(user_password)
            print("Your password has been encoded and stored!")
        if user_input == 3:
            break
