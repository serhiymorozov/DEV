# coding: utf-8
def game_core_v2(number):
    '''Реализуем алгоритм бинарного поиска
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    low_limit = 1
    high_limit = 100
    predict = (low_limit + high_limit)//2 #Вычисляем предполагаемое число
    while number != predict:
        count+=1
        if number > predict:              #Если загаданное число больше преполагаемого
            low_limit = predict + 1       #Вычисляем новую границу диапазона поиска
            predict = (low_limit + high_limit)//2
        elif number < predict:            #Если загаданное число меньше преполагаемого
            high_limit = predict - 1      #Вычисляем новую границу диапазона поиска
            predict = (low_limit + high_limit)//2
    return(count) # выход из цикла, если угадали


import numpy as np
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы наш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v2)
