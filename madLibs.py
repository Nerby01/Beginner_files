#codint=cp1251
from random import randrange

mads = {
    'noun':['птица', 'машина', 'самолёт','компьютер','мороженое'], 
    'adjective':['крутой', 'красный', 'большой', 'узкий', 'умный'], 
    'verb':['спрыгнул', 'бегал', 'шёл', 'заправлял', 'решал'], 
    'numeral':['первый', 'десятый', 'второй', 'сотый', 'последний'], 
    'pronoun':['я', 'ты', 'он', 'она', 'оно', 'они', 'вы', 'мы'], 
    'adverb':['здесь', 'там', 'нигде', 'никак', 'зачем', 'тогда'], 
    'predicative':['одеты', 'красив', 'врачом', 'президентов', 'работником'],
    'participle':['прочитанный', 'посеяный', 'разбросаны', 'собраны', 'построены', 'решены']
    }

string_ = input('Введите текст, а также в фигурных скобках { } обозначьте слово какой части речи вставить:\n')

# поиск вхождений в строку фигурных скобок { }
frame_1 = [i for i in range(len(string_)) if string_.startswith('{',i)]
frame_2 = [i for i in range(len(string_)) if string_.startswith('}',i)]

# инициализация первой подстроки
try:
    first_substr = string_[0:frame_1[0]]
except:
    exit('\nРезультат:\n{0}'.format(string_))
res = first_substr

i,j = 0,0 # i for frame_1 and j for frame_2

while j < len(frame_2):

    if i+1 < len(frame_1):
        substr = string_[frame_2[j] + 1:frame_1[i + 1]] # присваивается средняя подстрока
    else:
        substr = string_[frame_2[j] + 1:]             # присваивается последняя подстрока

    word_rand = len( mads [string_ [frame_1[i] + 1 :frame_2[j]]]) # количество слов в части речи
    word = mads[ string_[ frame_1[i] + 1 :frame_2[j] ]] [randrange(0, word_rand)] # выбирается рандомное слово
    res = res + word + substr
    i += 1
    j += 1

print('\nРезультат:\n{0}'.format(res))