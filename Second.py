# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def game_with_player (score, player_one, player_two):
    if score > 0:
        gamer = int(input(f"{player_one}, введите число от 0 до 28: "))
        if (gamer > 28) or (gamer < 0):
            print("Ошибка, введите число от 0 до 28")
            gamer = int(input(f"{player_one}, введите число от 0 до 28: "))
            while (gamer > 28) or (gamer < 0):
                print("Ошибка, введите число от 0 до 28")
                gamer = int(input(f"{player_one}, введите число от 0 до 28: "))
        score = score - gamer
        print(score)
        if score <= 0:
            print(f"Конец! Выйграл {player_one}")
        game_with_player(score, player_two, player_one)

def game_with_cpu (score, player_one, player_two):
    if score > 0:
        gamer = int(input(f"{player_one}, введите число от 0 до 28: "))
        if (gamer > 28) or (gamer < 0):
            print("Ошибка, введите число от 0 до 28")
            gamer = int(input(f"{player_one}, введите число от 0 до 28: "))
            while (gamer > 28) or (gamer < 0):
                print("Ошибка, введите число от 0 до 28")
                gamer = int(input(f"{player_one}, введите число от 0 до 28: "))
        score = score - gamer
        print(score)
        if score <= 0:
            print(f"Конец! Выйграл {player_one}")
        else:
            cpu_num = random.randint(1,28)
            print(f'Ход компьтера: {cpu_num}')
            score = score - cpu_num
            print(score)
            if score <= 0:
                print(f"Конец! Выйграл {player_two}")
            else:
                game_with_cpu(score, player_one, player_two)


player_one = 'Игрок 1'
player_two = 'Игрок 2'
score = 2021

start_game = int(input("Если исполользуется игра на двоих нажмите '2', если против компьтера нажмите 1: "))
if start_game == 2:
    print("Генерация очередности хода")
    first_game = random.randint(1,2)
    if first_game == 1:
        game_with_player(score, player_one, player_two)
    else:
        game_with_player(score,player_two, player_one)
else:
    second_player = 'CPU'
    game_with_cpu(score, player_one, second_player)
