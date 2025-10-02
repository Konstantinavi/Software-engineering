a = int(input("Введите целое число a (от 1 до 1000): "))
b = int(input("Введите целое число b (от 1 до 1000): "))
if 1 <= a <= 1000 and 1 <= b <= 1000:
    result = "a" if a > b else "b"
    print(result)
else:
    print("Не соответствует требованиям")