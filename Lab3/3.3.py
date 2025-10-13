prev = int(input("Введите предыдущие показания: "))
curr = int(input("Введите текущие показания: "))
used = curr - prev
total = 21
if used > 300 and used <= 600:
    total += (used - 300) * 0.06
elif used > 600 and used <= 800:
    total += 300 * 0.06 + (used - 600) * 0.04
elif used > 800:
    total += 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
average = total / used
print("Объем использованного газа:", used)
print("Сумма оплаты: ", round(total, 2))
print("Средняя цена за кубометр: ", round(average, 2))

