"""ДЗ 10-10."""

# # Бином Ньютона


# дз расписать бином ньютона до второй степени (с 0 ) и записать коэффициенты в треугольник паскаля

# https://drive.google.com/file/d/1qMy87TuJKmxhPODhW74bG_I15t_pLzUs/view?usp=share_link

# # Задачи

# Предположим, у нас есть мешок с 5 синими шарами, 3 зелеными шарами и 2 красными шарами. Мы случайным образом вытаскиваем один шар из мешка. Какова вероятность того, что выбранный шар будет синим?

# P(A) = 5/10 = 0.3

# Задача на теорему сложения вероятностей
#
# Задача: В корзине 4 яблока и 6 апельсинов. Какова вероятность того, что случайно выбранный фрукт будет либо яблоком, либо апельсином?

# P(A) = 4/10 + 6/10 = 1

# задачи на зависимые события
#
# Задача: В коробке находятся 5 синих и 4 красных шарика. Мы случайно вытаскиваем два шарика один за другим без возврата. Какова вероятность того, что первый шар будет синим, а второй — красным?

# P(A) = 5/9 * 4/8 = 20/72 = 0.278

# Формула полной вероятности
#
# Формула полной вероятности применяется, когда событие может произойти через несколько взаимно исключающих событий (гипотез), и нам нужно найти вероятность этого события с учётом всех возможных путей его наступления.
#
# Задача: Предположим, что у нас есть три коробки:
#
#     В первой коробке 3 белых и 2 черных шара.
#     Во второй коробке 1 белый и 1 черный шар.
#     В третьей коробке 4 белых и 3 черных шара.
#
# Случайным образом выбирается одна коробка, и из неё случайно вытаскивают один шар. Какова вероятность того, что этот шар будет белым?

# A0 = выбрали первую коробку
#
# A1 = выбрали вторую коробку
#
# A2 = выбрали третью коробку
#
# A0 = A1 = A2 = 1/3
#
# B - извлечен белый шар
#
# P(B) = 1/3 * 3/5 + 1/3 * 1/2 * 1/3 * 4/7 = 0.5571428571428572

(1 / 3) * (3 / 5) + (1 / 3) * (1 / 2) + (1 / 3) * (4 / 7)

# Формула Байеса
#
# Формула Байеса позволяет находить условную вероятность гипотезы, исходя из известной вероятности наступившего события. Она позволяет "обновлять" вероятность гипотезы на основании новой информации.
#
# Задача: Предположим, что есть три автомастерские:
#
#     В первой ремонтируют 40% автомобилей, во второй — 35%, в третьей — 25%.
#     Вероятность того, что автомобиль будет отремонтирован правильно, составляет 90% для первой мастерской, 80% для второй и 75% для третьей.
#
# Какова вероятность того, что автомобиль был отремонтирован в первой мастерской, если известно, что ремонт был выполнен правильно?

# https://drive.google.com/file/d/1n2W16EoeUZQ-vEXDuZwFoQ5BZOUroAU-/view?usp=share_link
