import datetime, pyglet
from time import sleep

def check_int(value: int, type: int):
    'type = 1 for hour check or 2 for minute'

    if type == 1 and ((int(value) // 24) > 0):
        value = int(value) % 24
    elif type == 2 and ((int(value) // 60) > 0):
        value = int(value) % 60
    return value

music = pyglet.resource.media('your_file.mp3')
print('Введите время срабатывания будильника')

while 1:

    hour, minute = str(input('Час: ')), str(input('Минута: '))

    #Проверка формата введённых значений пользователем
    try:
        hour = int(hour)
        minute = int(minute)
    except ValueError:
        print('Введите время в целочисленном формате!')
        continue

    #Получение остатка от деления, если часы или минуты больше 24 и 60 соотв.
    hour = check_int(int(hour), 1)
    minute = check_int(int(minute), 2)
    
    time = datetime.datetime.now()
    
    if (str(time.hour) == str(hour)
     and str(time.minute) == str(minute)):
        print('Работает')
        music.play()
        break
    sleep(1)

pyglet.app.run()