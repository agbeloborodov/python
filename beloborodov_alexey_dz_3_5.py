import random
from random import randrange, choice

def get_jokes(num_joks):
    """ the function generates a given number of jokes, making a random selection from the lists """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    lst_petrosjan = []
    for item in range(num_joks):
        lst_petrosjan.append(f' {random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return lst_petrosjan

jokes = int(input(' Введите желаемое количество петросянизмов: ',))
print(get_jokes(jokes))