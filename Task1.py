num = int(input("Введите номер дня недели: "))
if num > 7 or num < 1:
    print("Неверный день")
elif num == 6 or num == 7:
    print("Это выходной день")
else:
    print("Это будний день")