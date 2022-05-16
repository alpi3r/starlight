number = 1
count = 0
while number != 0:
    number = int(input("Введите число: "))
    if number %4 == 0 and number > count and number != 0:
        count = number
print(f"Максимальное число кратное 4: {count}")
# by alpi3r