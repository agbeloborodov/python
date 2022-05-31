

def num_translate_adv(number_eng, ord_of_symb):
    """ The function of translating numbers in the range 1..10 from english to russian """
    dict_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if 96 < ord_of_symb < 123 or ord_of_symb <=64 or ord_of_symb >=91:
        number_rus = dict_translate.get(number_eng)
    elif 64 < ord_of_symb < 91:
        number_eng = number_eng.lower()
        number_rus = dict_translate.get(number_eng).title()
    return number_rus


item = input('Введите число в диапазоне 1..10 на английском языке с любой буквы : ', )
print(num_translate_adv(item, ord(item[0])))
