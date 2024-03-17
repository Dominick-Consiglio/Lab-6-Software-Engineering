# Dominick Consiglio

def encode(password):
    encoded_password = ""
    for n in password:
        encoded_password += (str(int(n)+3))[-1]
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = (int(digit) - 3) % 10
        decoded_password += str(decoded_digit)
    return decoded_password


def main():
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif option == "3":
            break
        else:
            print("Invalid Option. Please input an integer 1, 2, or 3.\n")


if __name__ == '__main__':
    main()