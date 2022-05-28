retro_weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('Исходный список: ', 'id =', id(retro_weather), '   ', retro_weather)
item = 0
while item < len(retro_weather):
    if retro_weather[item].isnumeric():
        retro_weather[item] = '"' + retro_weather[item].zfill(2) + '"'
    elif retro_weather[item].startswith('+') or retro_weather[item].startswith('-'):
        retro_weather[item] = '"' + retro_weather[item].zfill(3) + '"'
    item +=1
print('Полученный список: ', 'id =', id(retro_weather),'   ', retro_weather)
retro_weather = ' '.join(retro_weather)
print('Полученная строка: ', 'id =', id(retro_weather), '   ', retro_weather)