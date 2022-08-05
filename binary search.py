from random import randint

list_ = []

for i in range(10):
    list_.append(randint(1,100))

list_.sort()
print('Исходник: ',list_)

try:
    value_ = int(input('Введите число для поиска: '))
except:
    exit('Надо было ввести целочисленное...')

middle = len(list_)//2
low = 0
high = len(list_) - 1



while list_[middle] != value_ and low <= high:
    if value_ > list_[middle]:
        low = middle + 1
    else:
        high = middle - 1
    middle = (low + high)//2

if low > high:
    print('Нет значения...')
else:
    print('ID = ', middle)