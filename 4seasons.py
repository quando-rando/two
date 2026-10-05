s = input('Введите время года: ')
s = s.lower()
if s == 'лето':
    print(f"{s.capitalize()} - заебись")
elif s == "осень":
    print(f"{s.capitalize()} - класс")
elif s == "зима":
    print(f"{s.capitalize()} - тоже")
elif s == "весна":
    print(f"{s.capitalize()} - отлично")
else:
    print(f"{s} - это не время года")
print()