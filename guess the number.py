#codint=cp1251
from random import randrange

i = int(input('Введите число для ограничения: '))
while True:
    n = int(input('Ну что, начнем? Какое число я загадал???\n'))
    n_2 = randrange(0,i)
    if n == n_2:
        print('Угадал...')
    else:
        print('Не верно :)')