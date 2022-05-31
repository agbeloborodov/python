limit_odd_cube = int(input('Введите верхнюю границу списка: ', ))
odd_cube = []
i = 0
while i <= limit_odd_cube:
    if (i % 2) > 0:
        odd_cube.append(i**3)
    i += 1
print('Список кубов нечётных чисел от 0 до 100: ', odd_cube)

result = 0
for i in (odd_cube):
    sum = 0
    j = i
    while (j != 0):
        sum = sum + j % 10
        j = j // 10
    if not (sum % 7):
        print('У изначального элемента списка ', i, 'сумма его цифр нацело делится на 7 ')
        result = result + i
print('Сумма тех чисел изначального списка, сумма цифр которых делится нацело на 7, равна ', result)

i = 0
while i < len(odd_cube):
    odd_cube[i] = odd_cube[i] + 17
    i += 1
print('Список увеличенных на 17 кубов нечётных чисел от 0 до 100: ', odd_cube)

i = 0
result = 0
for i in (odd_cube):
    sum = 0
    j = i
    while (j != 0):
        sum = sum + j % 10
        j = j // 10
    if not (sum % 7):
        print('У нового элемента списка  ', i, ' сумма его цифр нацело делится на 7 ')
        result = result + i
print('Сумма тех чисел нового списка, сумма цифр которых делится нацело на 7, равна ', result)











