import random
import string

def generate(length, include_symbols):
    """Generate passwords with requested specifications."""
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    symbols = ['!','@','#','$','%','&','?','*']
    password = []

    if include_symbols:
        for i in range(length - 1):
            char_type = random.choice([numbers, lower, upper, symbols])
            char = random.choice(char_type)
            password.append(char)

        last_char = random.choice(symbols)
        password.append(last_char)
        random.shuffle(password)

    else:
        for i in range(length):
            char_type = random.choice([numbers, lower, upper])
            char = random.choice(char_type)
            password.append(char)
   
    return ''.join(password)


def get_length():
    """Get the length of requested password. Check correctness of user inputs."""
    while True:
        try:
            length = int(input("Password length: "))
        except ValueError:
            print("That is not a number, please try again. (Enter a number between 8 and 20.)")
            continue

        if length > 20:
            print("That is too long, please try again. (Enter a number between 8 and 20.)")
        elif length < 8:
            print("That is too short, please try again. (Enter a number between 8 and 20.)")
        else:
            return length


if __name__ == "__main__":
    length = get_length()

    symbol = input("Include symbols? (y/n): ")

    if symbol.lower() == 'y':
        password = generate(length, True)
    else:
        password = generate(length, False)

    print("Your password is: ", password)
