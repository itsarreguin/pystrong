import random

def password():
    upper = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'
    ]
    lower = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'
    ]
    numbs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    chars = [
        '*', '+', '/', '@', '?', '!', '[', '{', '(', ')', '}', ']', ';', '>', '<', '&', '$', '#', '¿', '¡'
    ]

    create = upper + lower + numbs + chars

    password = []

    for _ in range(20):
        select_rand = random.choice(create)
        password.append(select_rand)
    password = ''.join(password)
    
    return password


def main():
    new_password = password()
    print(f'New password: {new_password}')


if __name__ == '__main__':
    main()