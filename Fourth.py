# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('txt_for_zad_4', 'w', encoding="utf-8") as data:
    data.write("ffffaaaapppppkkkdiiiwwwnnccc")

temp_str = ''
zip_str = ''
path = 'txt_for_zad_4'
temp_str_zip = ''
finish_str = ''

with open('txt_for_zad_4', 'r', encoding="utf-8") as data:
    for line in data:
        temp_str = line

print(temp_str)

i=0
while i< len(temp_str):
    count= 1
    while (i+1<len(temp_str)) and (temp_str[i] == temp_str[i+1]):
        count+=1
        i+=1
    zip_str += str(count) + temp_str[i]
    i+=1
    count=1

with open('txt_for_zad_4_zip', 'w', encoding="utf-8") as data:
    data.write(zip_str)

with open('txt_for_zad_4_zip', 'r', encoding="utf-8") as data:
    for line in data:
        temp_str_zip = line

print(temp_str_zip)

k=0

while k< len(temp_str_zip):
    finish_str += temp_str_zip[k+1]*int(temp_str_zip[k])
    k+=2

print(finish_str)
