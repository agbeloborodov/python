from copy import deepcopy
lst_of_prices = [45.05, 34.47, 25.89, 98.44, 7.3, 2.8, 34.1, 62.99, 56.9, 29.7]
print('id первоначального списка =', id(lst_of_prices), '   Список цен:', lst_of_prices)
print(' ')
str_of_prices = ''
for item in lst_of_prices:
    str_of_prices = str_of_prices + str(int(item - (item % 1))).zfill(2) + 'руб.' + str(int(round((item % 1) * 100, 2))).zfill(2) + 'коп.  '
print('Строка цен, приведённая к понятному виду: ', str_of_prices)
print ('id первоначального списка =', id(lst_of_prices), '   Список цен:', lst_of_prices)
print(' ')
str_of_prices = ''
lst_of_prices.sort()
for item in lst_of_prices:
    str_of_prices = str_of_prices + str(int(item - (item % 1))).zfill(2) + 'руб.' + str(int(round((item % 1) * 100, 2))).zfill(2) + 'коп.  '
print('Строка цен, упорядоченная по возрастанию: ', str_of_prices)
print ('id первоначального списка =', id(lst_of_prices), '   Список цен:', lst_of_prices)
print(' ')
lst_of_prices_rev = deepcopy(lst_of_prices)
lst_of_prices_rev.sort(reverse=True)
str_of_prices = ''
for item in lst_of_prices_rev:
    str_of_prices = str_of_prices + str(int(item - (item % 1))).zfill(2) + 'руб.' + str(int(round((item % 1) * 100, 2))).zfill(2) + 'коп.  '
print('Строка цен, упорядоченная по убыванию: ', str_of_prices)
print('id первоначального списка =', id(lst_of_prices), '   Список цен:', lst_of_prices)
print(' ')
str_of_prices = ''
for item in lst_of_prices_rev[:5]:
    str_of_prices = str_of_prices + str(int(item - (item % 1))).zfill(2) + 'руб.' + str(int(round((item % 1) * 100, 2))).zfill(2) + 'коп.  '
print('Строка цен пяти самых дорогих товаров, упорядоченная по убыванию: ', str_of_prices)