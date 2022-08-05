#coding=cp1251

import random, string

def password_gen(length):
    letters = string.ascii_lowercase
    symbols = [',' , '.' , '_' , '!' , '?']

    rand_str = ''.join(random.choice(letters) for i in range(length))
    rand_symb_index = random.randint(0, len(symbols) - 1)
    rand_symbol = symbols[rand_symb_index]
    
    password = rand_str.capitalize() + rand_symbol + str(random.randrange(0, 100))
    return password

print(password_gen(20))