import pymorphy2

import random

vowels = "АЕЄИІЇОУЮЯаеєиіїоуюя"
not_vowels = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ"

def random_symbol(all_symbols):
    return random.choice(all_symbols)

def random_word():
    word_length = random.randint(4, 15)
    word = []

    use_vowel = random.choice([True, False])

    for i in range(word_length):
        if use_vowel:
            char = random_symbol(vowels)
        else:
            char = random_symbol(not_vowels)
        if i == 0:
            char = char.upper()
        else:
            char = char.lower()

        word.append(char)
        use_vowel = not use_vowel

    return "".join(word)

morph = pymorphy2.MorphAnalyzer(lang='uk')


def check_word_uk(random_slovo):
    parsed = morph.parse(random_slovo)
    return any(p.is_known for p in parsed)

for i in range (100000):
    random_slovo = random_word()
    if check_word_uk(random_slovo):
        print(f"{random_slovo}")
