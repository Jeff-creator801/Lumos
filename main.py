def is_masculine(word):
    """Определяет, является ли слово мужского рода."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Класс 1: заканчивается на "a" → женский
    if word.endswith('a'):
        return False
    
    # Класс 3: заканчивается на "ion" → женский
    if word.endswith('ion'):
        return False
    
    # Классы 2a и 2b: оканчивается на "i" или "z" с гласной перед ней → женский
    if len(word) >= 2 and word[-1] in ['i', 'z']:
        if word[-2] in vowels:
            return False
    
    # Все остальные случаи → мужской
    return True

def generate_words():
    """Генерирует слова для обучения."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y']
    
    words = set()
    result = []
    
    # 1. Слова мужского рода (60 слов)
    masculine_count = 0
    while masculine_count < 60:
        # Генерируем слова разной длины от 2 до 10 букв
        length = (masculine_count % 9) + 2  # от 2 до 10
        
        # Чередуем согласные и гласные для разнообразия
        word = ''
        for i in range(length):
            if i % 2 == 0:
                word += consonants[(masculine_count + i) % len(consonants)]
            else:
                word += vowels[(masculine_count + i) % len(vowels)]
        
        # Убедимся, что слово мужского рода
        # Добавляем окончания, которые точно дадут мужской род
        if masculine_count % 4 == 0:
            word += 'b'
        elif masculine_count % 4 == 1:
            word += 'c'
        elif masculine_count % 4 == 2:
            word += 'd'
        else:
            word += 'e'
        
        if word not in words and len(word) >= 2 and is_masculine(word):
            words.add(word)
            result.append(f"{word} m")
            masculine_count += 1
    
    # 2. Слова женского рода класса 1 (20 слов) - оканчиваются на "a"
    feminine_class1 = 0
    while feminine_class1 < 20:
        length = (feminine_class1 % 8) + 3  # от 3 до 10
        word = ''
        for i in range(length - 1):  # последняя буква будет "a"
            if i % 2 == 0:
                word += consonants[(feminine_class1 + i + 100) % len(consonants)]
            else:
                word += vowels[(feminine_class1 + i + 100) % len(vowels)]
        word += 'a'  # Класс 1
        
        if word not in words and len(word) >= 2:
            words.add(word)
            result.append(f"{word} f")
            feminine_class1 += 1
    
    # 3. Слова женского рода класса 2a (10 слов) - оканчиваются на "i" с гласной перед ней
    feminine_class2a = 0
    vowel_index = 0
    while feminine_class2a < 10:
        length = (feminine_class2a % 7) + 4  # от 4 до 10
        word = ''
        for i in range(length - 2):  # предпоследняя и последняя буквы будут добавлены
            if i % 2 == 0:
                word += consonants[(feminine_class2a + i + 200) % len(consonants)]
            else:
                word += vowels[(feminine_class2a + i + 200) % len(vowels)]
        
        # Добавляем гласную и "i"
        word += vowels[vowel_index % len(vowels)]  # предпоследняя - гласная
        word += 'i'  # последняя - "i" (класс 2a)
        
        vowel_index += 1
        
        if word not in words and len(word) >= 2:
            words.add(word)
            result.append(f"{word} f")
            feminine_class2a += 1
    
    # 4. Слова женского рода класса 2b (10 слов) - оканчиваются на "z" с гласной перед ней
    feminine_class2b = 0
    vowel_index = 0
    while feminine_class2b < 10:
        length = (feminine_class2b % 7) + 4  # от 4 до 10
        word = ''
        for i in range(length - 2):  # предпоследняя и последняя буквы будут добавлены
            if i % 2 == 0:
                word += consonants[(feminine_class2b + i + 300) % len(consonants)]
            else:
                word += vowels[(feminine_class2b + i + 300) % len(vowels)]
        
        # Добавляем гласную и "z"
        word += vowels[vowel_index % len(vowels)]  # предпоследняя - гласная
        word += 'z'  # последняя - "z" (класс 2b)
        
        vowel_index += 1
        
        if word not in words and len(word) >= 2:
            words.add(word)
            result.append(f"{word} f")
            feminine_class2b += 1
    
    # 5. Слова женского рода класса 3 (20 слов) - оканчиваются на "ion"
    feminine_class3 = 0
    while feminine_class3 < 20:
        length = (feminine_class3 % 7) + 5  # от 5 до 11, чтобы было место для "ion"
        word = ''
        for i in range(length - 3):  # последние 3 буквы будут "ion"
            if i % 2 == 0:
                word += consonants[(feminine_class3 + i + 400) % len(consonants)]
            else:
                word += vowels[(feminine_class3 + i + 400) % len(vowels)]
        word += 'ion'  # Класс 3
        
        if word not in words and len(word) >= 2:
            words.add(word)
            result.append(f"{word} f")
            feminine_class3 += 1
    
    return result

# Генерируем и записываем слова в файл
words_with_gender = generate_words()

# Записываем в файл output.txt
with open('output.txt', 'w', encoding='utf-8') as f:
    for line in words_with_gender:
        f.write(line + '\n')

print("Файл output.txt успешно создан с 120 словами:")
print(f"- 60 слов мужского рода")
print(f"- 20 слов женского рода класса 1 (оканчиваются на 'a')")
print(f"- 10 слов женского рода класса 2a (оканчиваются на 'i' с гласной перед ней)")
print(f"- 10 слов женского рода класса 2b (оканчиваются на 'z' с гласной перед ней)")
print(f"- 20 слов женского рода класса 3 (оканчиваются на 'ion')")
print(f"Всего уникальных слов: {len(words_with_gender)}")
