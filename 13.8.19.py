tickets = int(input("Введите количество человек "))  # получаем количество билетов
money = 0
for i in range(tickets):
    age = int(input("\nВозраст = "))
    if age < 18:
        money += 0
        print("Бесплатный билет")                   # вывод цены билета
    elif 18 <= age < 25:
        money += 990
        print("Стоимость билета составляет = 990 руб.")
    elif age >= 26:
        money += 1390
        print("Стоимость билета составляет = 1390 руб.")
if tickets > 3:
    diskount = (money/100) * 10                       # скидка 10%
    print("\nИтоговая стоимость билетов со скидкой составляет = ", int(money - diskount))
else:
    print("\nСтоимость всех билетов составляет = ", int(money))