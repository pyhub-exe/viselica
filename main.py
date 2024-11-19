import random
russian = ['собака','слон','кот','яблоко','дом','пылесос', 'воспользовавшийся','высокопревосходительство', 'витязь','переосвидетельствовать']
english = ['dog','cat', 'house', 'dad', 'banana', 'door', 'underground', 'defenestration', 'education', 'university']

spaces = []
used = []
min = 0
max = 0
used = []

def viselcia():
    flag = False
    attemps = 0
    guessedlet = 0
    words = []
    print('                     Виселица by kita v1.0.2')
    print('''            ___________________________________________
                        Обновление 1.0.2:
                        Что нового:
    -Добавлен выбор языков, на котором будут загаданы слова
    -Добавлен выбор сложности слов
    -Добавлена проверка, было ли уже введена буква
    -Исправлены ошибки
            _____________________________________________''')
    print('Здравствуйте! Это известная игра "Виселица". Для начала, выберите язык, на котором будут загаданы слова(русский/английский)')
    choose = input('Введите язык из скобок маленькими буквами:   ').lower()
    if choose == 'русский':
        words = russian

    elif choose == 'английский':
        words = english
    print(f'Ваш выбор: {choose}. Теперь выберем сложность!(легко/сложно) ')
    lvl = input('Выберите сложность:  ')
    if lvl == 'сложно':
        min = 6
        max =  9
    else:
        min = 0
        max = 5

    print('Я вас понял. Ну что, приступаем!')
    guesed = words[random.randint(min, max)]
    print(f'В слове {len(guesed)} букв')
    for i in range(len(guesed)):
        spaces.append('|_|')
    while attemps < 11 and flag is False:
        for i in range(len(guesed)):
            print(spaces[i], end = '')
        print()
        print('Введите букву...')
        letter = input()
        if letter.lower() in list(guesed):

            if letter in used:
                print('Буква уже введена -_-')
                continue
            for i in range(len(guesed)):
                if list(guesed)[i] == letter:
                        used.append(list(guesed)[i])
                        spaces[i] = f'|{letter}|'

                        if '|_|' not in spaces:
                            print('Вы выиграли!!!')
                            print(f'Вы потратили {attemps} попыток')
                            flag = True
                            break

            print('угадали')

        else:
            print('Такой буквы нет(')
            attemps += 1
        if attemps == 1:
            print('''
                     _______ 
            ''')
        if attemps == 2:
            print('''
                     
                    |      
                    |      
                    |       
                 _______  
            ''')
        if attemps == 3:
            print('''
                     _______
                    |      
                    |      
                    |      
                 _______  
            ''')
        if attemps == 4:
            print('''
                     _______
                    |      |
                    |      
                    |       
                 _______  
            ''')
        if attemps == 5:
            print('''
                     _______
                    |      |
                    |      0
                    |       
                 _______  
            ''')
        if attemps == 6:
            print('''
                     _______
                    |      |
                    |      0
                    |      | 
                 _______  
            ''')
        if attemps == 7:
            print('''
                     _______
                    |      |
                    |      0
                    |     /| 
                 _______  
            ''')
        if attemps == 8:
            print('''
                     _______
                    |      |
                    |      0
                    |     /|\\
                 _______  
            ''')
        if attemps == 9:
            print('''
                     _______
                    |      |
                    |      0
                    |     /|\\
                 _______  /
            ''')
        if attemps == 10:
            print('''
                     _______
                    |      |
                    |      0
                    |     /|\\
                 _______  / \\
            ''')
            print('Вы проиграли(((')
            print(f'Это было слово {guesed}')
            attemps += 1

viselcia()