import random
import string

from wtforms.validators import length


def random_number():
    print("Random Number: ", random.randint(1, 100))
    print("==============================")


def random_list():
    print("Random List: ", random.sample(range(1, 50), 5))
    print("==============================")


def random_password():
    length = int(input("Password Length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    print("Generated Password: ", ''.join(random.choice(chars) for _ in range(length)))
    print("==============================")


def random_otp():
    print("OTP:", random.randint(100000, 999999))
    print("==============================")


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            random_number()
        elif ch == 2:
            random_list()
        elif ch == 3:
            random_password()
        elif ch == 4:
            random_otp()
        elif ch == 5:
            break