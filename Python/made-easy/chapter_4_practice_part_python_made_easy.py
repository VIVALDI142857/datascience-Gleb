"""Глава 4, практическая часть."""

# 1 . Питер получает зарплату 12 ООО в месяц. Напишите код для вычисления его сбе­режений к концу года, если он будет откладывать 20% своей зарплаты каждый месяц.

salary: int = 12000  # зарплата Питера
months: int = 12  # количество месяцев в году
percent: float = 0.2  # откладывает каждый месяц
total_saved: float = salary * months * 0.2  # исходя
# из свойств процентов
# мы можем вычислить процент от общей суммы,
# заработанной за год,
# вместо того, чтобы вычислять процент каждый месяц.

# 2. Расстояние между Мумбаи и Дели составляет 1422 км.
# Если Сундар едет на ма­шине со средней скоростью 72 км/ч,
# сколько времени ему потребуется, чтобы преодолеть это расстояние?

distance: int = 1422
avg_speed: int = 72
time: float = distance / avg_speed
print(time, "часов потребуется Сундару")

# 3. Температура тела человека находится в диапазоне от 97 до 99 по Фаренгейту.
# Как этот диапазон будет выглядеть в градусах Цельсия?
#
# C = (F−32) × 5/9
# ​
#
#

farengate: list[int] = [97, 98, 99]
for temp in farengate:
    celsium = (temp - 32) * 5 / 9
    print(celsium)

# 4. Пусть дано шестизначное число. Напишите программу для вычисления суммы всех цифр этого числа.
#
# Рассмотрим на примере числа 895623

Number: int = 895623
sum_list: list[int] = []
for Digit in str(Number):
    sum_list.append(int(Digit))
sum(sum_list)

# 5. У нас есть данные о месячных продажах 5 книжных магазинов в Бруклине:
#
# А = $6 500, В = $8 000,
#
# С = $12 000, D = $4 900 и Е = $5 600.
#
# Предполагая, что в Бруклине всего 5 книжных магазинов, узнайте рыночную долю каждого магазина. Также проверьте, какой будет сумма рыночных долей всех магазинов. (Рыночная доля означает отношение одного участника ко всем остальным.)

# +
shop_dict: dict[str, int] = {
    "shop_A": 6500,
    "shop_B": 8000,
    "shop_C": 12000,
    "shop_D": 4900,
    "shop_E": 5600,
}

for shop, sales in shop_dict.items():
    print(shop, sales / (sum(shop_dict.values()) - sales))
# -

# 6. Среднее значение трех чисел равно 45. Первое число больше среднего значения настолько же, насколько второе число меньше среднего значения. Найдите третье число.

# составляем уравнение, исходя из имеющихся данных:
#
# 45 + (45 - num2) = num1
#
# раскрываем скобки
#
# 90 - num2 = num1
#
# переносим все переменные в одну сторону:
#
# num1 + num2 = 90
#
# С помощью домножения среднего числа на количество чисел находим сумму трех чисел, из которой вычитаем сумму первого и второго числа, чтобы найти третье.
#
# 45 * 3 = 135 => num3 = 135 - 90 = 45

# 7. Джон покупает мобильный телефон за 1 800 в Калькутте и продает его в Мум­баи с прибылью 25%. Если его накладные расходы составляют 5% от цены продажи, то какова цена продажи?
#
# 1800 * 1.25 = 2250 - цена продажи без накладных расходов
#
# цена продажи = 2250 + 0.05 * цена продажи
#
# 0.95 * цена продажи = 2250
#
# цена продажи = 2250 / 0.95 = 23682.4

# ![image.png](attachment:image.png)

diagonal: int = 5
volume: float = diagonal**3 / 3 * 3**0.5
area: int = 2 * diagonal**2
volume, area

# 9. Три металлических куба с ребрами длиной 3, 4 и 5 см соответственно пере­плавляются в один куб. Найдите длину ребра нового куба.

# +
diagonal3: int = 3
diagonal4: int = 4
diagonal5: int = 5
volume3: int = diagonal3**3
volume4: int = diagonal4**3
volume5: int = diagonal5**3

volume_total: int = volume3 + volume4 + volume5
diagonal_total: float = (volume_total) ** 0.33
diagonal_total


# -

# 10. Дано шестизначное число. Напишите программу для получения числа с обрат­ным порядком цифр.
#
# Напишем функцию для обращения 6ти значных чисел


def reversible(number: int) -> int:
    """Reverse the input int.

    Returns:
        int: The reversed int.
    """
    reversed_num: str = ""
    num_list: list[str] = []
    for digit in str(number):
        num_list.append(digit)
    if len(num_list) == 6:
        reversed_num = "".join(num_list[::-1])
    return int(reversed_num)


amount: int = 223455
reversible(amount)
