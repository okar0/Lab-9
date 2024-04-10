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
        encoded = encoder(password)
        print(f"The encoded password is {encoded}")

    elif option == '2':
        password = input("Please enter your password to decode: ")
        decoded = decoder(password)  # You need to implement a decoder function
        print(f"The decoded password is {decoded}")

    elif option == '3':
        exit()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
