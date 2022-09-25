# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('txt_for_zad_1', 'w', encoding="utf-8") as data:
    data.write("Абсоабвлютно невозвабвможно абвосуществить Выполнение задания один для пятого семинара по Python табвк кабвк этоабв нереальнабво")

find = "абв"
temp_str = ''
temp_list = []
list = []
finish_str = ''

path = 'txt_for_zad_1'
with open('txt_for_zad_1', 'r', encoding="utf-8") as data:
    for line in data:
        temp_str = line

temp_list = temp_str.split(" ")

for k in range(len(temp_list)):
    for i in range(len(temp_list[k])):
        if (temp_list[k][i] == find[0]) and (i+2 <= len(temp_list[k])):
            if (temp_list[k][i+1] == find[1]):
                if (temp_list[k][i+2] == find[2]):
                    list.append(k)

list.reverse()

for k in range(len(list)):
    temp_list.pop(list[k])

for i in temp_list:
    finish_str += i+ " "
    
with open('txt_for_zad_1_finish', 'w', encoding="utf-8") as data_finish:
    data_finish.write(finish_str)
