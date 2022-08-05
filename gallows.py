#codint=cp1251

string = list('виселица'.lower())

while True:
    remove_char = input('Угадайте букву в слове:\n').lower()
    if remove_char in string:
        string.remove(remove_char)
    elif len(string) == 0:
        exit('Игра закончена')
    else:
        print('Не угадал')