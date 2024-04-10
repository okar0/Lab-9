def encoder(password):
    encoded_password = ""
    for char in str(password):
        char = int(char)
        char += 3
        if char >= 10:
            char -= 10
        encoded_password += str(char)
    return encoded_password

def main():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")
    option = input("Please enter an option: ")
    if option == '1':
        password = input("Please enter your password to encode: ")
        print(f"Your password has been encoded and stored!")

    elif option == '2':
        print(f"The encoded password is {encoder(password)}, and the original password is {password}")

    elif option == '3':
        exit()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
