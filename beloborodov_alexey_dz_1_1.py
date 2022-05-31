duration = int(input(' Введите количество секунд, требуемых перевода в "человеческий" формат: ', ))
if 0 <= duration < 60:
    print(duration, 'сек.')
elif 60 <= duration < 3600:
    print(duration // 60, 'мин.', duration % 60, 'сек.')
elif 3600 <= duration < 86400:
    print(duration // 3600, 'час.', (duration - (duration // 3600) * 3600) // 60, 'мин.', duration % 60, 'сек.')
elif 84600 <= duration :
    print(duration // 84600, 'дн.', (duration - (duration // 86400) * 86400) // 3600, 'час.', (duration - (duration // 3600) * 3600) // 60, 'мин.', duration % 60, 'сек.')
else:
    print('Ваш запрос нарушает на макроуровне ОТО нобелевского лауреата Альберта Энштейна')
