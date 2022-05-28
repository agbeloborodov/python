lst_of_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print ('id=', id(lst_of_employees), type(lst_of_employees), lst_of_employees)
for item in lst_of_employees:
    item = item.split(' ')
    item.reverse()
    print('Привет, ', item[0].title(), '         ', 'id=', id(item), type(item))
