# Ввод строки от пользователя
vvod_ot_polzovatelya = input("Введите строку: ")

# Если строка содержит больше одного символа, меняем местами первую и последнюю буквы
if len(vvod_ot_polzovatelya) > 1:
    modified_string = vvod_ot_polzovatelya[-1] + vvod_ot_polzovatelya[1:-1] + vvod_ot_polzovatelya[0]
else:
    # Если строка пустая или содержит только один символ, оставляем её без изменений
    modified_string =  vvod_ot_polzovatelya

# Вывод измененной строки
print("Измененная строка:", modified_string)