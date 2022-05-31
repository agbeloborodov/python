def num_translate(number_eng) :
    """ The function of translating numbers in the range 1..10 from english to russian """
    dict_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    number_rus = dict_translate.get(number_eng)
    return number_rus


item = input('Введите число в диапазоне 1..10 на английском языке с маленькой буквы : ',)
print(num_translate(item))