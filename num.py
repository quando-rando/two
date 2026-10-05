
num = 3
while num <= 43:
    print(num)
    num += 10

##################################

password = input("Введите пароль не менее 8 символов: ")
while len(password) < 8:
    print("Длина пароля меньше 8 символов")
    password = input("Введите пароль снова: ")
    print(password)
else:
    print("Пароль принят")


##################################

print("Введите параметры автомобиля по шаблону: ")
mod = input("Марка: ")
year = int(input("Год выпуска: "))
trip = int(input("Пробег: "))
price = int(input("Цена: "))
print(f'Марка: {mod}\nГод выпуска: {year} г\nПробег: {trip} км\nЦена: {price} руб\n')