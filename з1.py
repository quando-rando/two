# number = 3
#
# while number <= 43:
#     print(number)
#     number += 10
#

# password = input("Введите пароль: ")
#
# while len(password) < 8:
#     print("Пароль менее 8 символов.")
#     password = input("Введите пароль ещё раз: ")
#
# print("Пароль принят!")

mark, year, mileage, price = input("Введите параметры автомобиля: ").split()

print(f"Продается автомобиль\nМарка: {mark}\nГод выпуска: {year}\nПробег: {mileage}\nЦена: {price}")