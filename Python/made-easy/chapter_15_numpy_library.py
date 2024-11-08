"""Глава 15."""

import numpy as np

# **NumPy** (Numerical Python) - это библиотека Python с открытым исходным кодом, которая используется практически во всех областях науки и техники.
#
# В отличие от универсального Python, в который встроено множество структур дан­ных, в NumPy есть всего одна структура - многомерный массив и различные про­изводные объекты, в том числе матрицы.
#
# В основе NumPy лежит тип данных ndarray который представляет собой однород­ный многомерный массив, а также методы для эффективной работы с ним.
#
# # Разница между списком Python и массивом NumPy
#
# В NumPy есть огромное количество быстрых и эффективных способов создания массивов и обработки их числовых данных. Python позволяет хранить в одном спи­ ске данные разных типов, но в массиве NumPy все элементы должны быть одного типа. Математические операции, которые выполняются над массивами, были бы очень неэффективными, если бы элементы в массивах не бьли однородными.
#
#

# ![image.png](attachment:image.png)

# # Зачем нам NumPy?
#
# Массивы NumPy быстрее и компактнее, чем списки Python. Массив занимает меньше памяти и удобнее в использовании. NumPy использует намного меньше памяти для хранения данных и имеет механизм для явного задания типа данных, что позволяет еще больше оптимизировать код. NumPy работает быстрее, чем списки, потому что массивы NumPy занимают мень­ше места в памяти по сравнению со списками и, следовательно, быстрее загружа­ются.
#
# Есть еще одно преимущество массива NumPy в том, что он хранится в памяти не­ прерывно. Это означает, что данные хранятся без пробелов между ними. А вот спи­ски разрознены.
#
# # Массив NumPy
#
# Массив - это центральная структура данных библиотеки NumPy. Массив пред­ставляет собой таблицу значений, содержащую информацию о необработанных данных, о том, как найти элемент и как интерпретировать элемент. В массиве есть сетка элементов, которые можно индексировать разными способами. Все элементы имеют один тип, который сохраняется в атрибуте dtype.
#
# **Размерность массива**
#
# Иногда массивы называют ndarray, что является сокращением от англ. N-dimen­sional array (п-мерный массив). Здесь имеется в виду, что это просто массив с любым количеством измерений. Иногда также встречаются термины ID-массив (одномерный массив) и 2D-массив (двумерный массив). Класс NumPy ndarray используется для представления как матриц, так и векторов.
# Вектор представляет собой одномерный массив (вектор-строка или вектор­ столбец - это одно и то же).
# Матрица - это двумерный массив.
# Для трехмерных массивов или массивов более высокой размерности обычно ис­
# пользуется термин тензор.
#
# **Другие атрибуты массива**
#
# Массив обычно представляет собой контейнер фиксированного размера с элемен­тами одного типа и размера. Размерность массива и количество элементов в масси­ве определяются его формой. Форма массива- это кортеж неотрицательных целых чисел, которые определяют размеры по каждому измерению.
#
# В вашем массиве 2 оси. Первая ось имеет длину 2, а вторая ось - длину 3 .
# Как и в других контейнерах Python, к содержимому массива можно обращаться и изменять его с помощью индексации или среза. В отличие от типичных объектов­ контейнеров, разные массивы могут совместно использовать одни и те же данные, поэтому изменения, внесенные в один массив, могут быть видны и в другом мас­сиве.
#
# # Создание массива

np.array([])

# **Массивы из нулей, единиц и случайных чисел**
#
# Часто элементы массива изначально неизвестны, известен лишь его размер. Поэто­му в NumPy есть несколько функций для создания массивов с опеределенным на­чальным заполнителем. Это сводит к минимуму необходимость увеличения разме­ра массива в процессе работы, что требует немало ресурсов.
# Функция zeros() создает массив, заполненный нулями, функция ones() создает мас­сив, заполненный единицами. По умолчанию тип элементов таких массивов­ flоаt64.
#
# Функция empty() создает массив, начальное содержимое которого является случай­ ным и зависит от состояния памяти. Причина использования массива случайных чисел вместо нулей - это скорость. Но после этого нужно заполнить каждый эле­мент
#
# Часто бывают случаи, когда мы хотим, чтобы NumPy сам задал значения массива. В NumPy есть также класс random.Generator для генерации случайных чисел. Вам достаточно лишь передать количество элементов, которые вы хотите сгенерировать

# ![image.png](attachment:image.png)

# **Массив из диапазона значений**
#
# Для создания последовательностей чисел в NumPy есть функция np.arange(), работающая аналогично встроенной функции range() в Python, но возвращающая массив.
#
# Когда в arange() передают аргументы с плавающей точкой, обычно невозможно предсказать количество полученных элементов из-за конечной точности этого формата. Поэтому в таких случаях лучше использовать функцию linspace() , кото­рая вместо шага принимает в качестве аргумента количество элементов.
#
# **Указание типа данных массива**
#
# По умолчанию - np.float64
#
# # Вывод массивов
#
# Одномерные массивы выводятся как строки, дувмерные как матрицы, трехмерные = как списки матриц
#
# # Сортировка, добавление и удаление элементов массива
#
#
#

# **Cортировка**

x_ = np.array([1, 4, 2, 6, 5, 8])
y_ = np.sort(x_)
y_

# **Сложение (конкатенация)**

np.concatenate((x_, y_))

# **Удаление**
#
# Чтобы удалить элементы из массива, просто используйте индексирование и укажи­ те элементы, которые вы хотите сохранить.

# # Форма и размер массива
#
# У массивов есть целый ряд важных атрибутов.
#
# ♦ ndarray.ndirn - это количество осей или размерность массива.
#
# ♦ ndarray.size - это общее количество элементов массива. Это произведение раз­меров массива.
#
# ♦ ndarray.shape - кортеж целых чисел, в котором хранятся размеры массива по каждому измерению.
#
# #  Изменение формы
#
# Метод ndarray.reshape() позволяет изменить форму массива без изменения данных. Просто помните, что, когда вы используете метод reshape() , массив, который вы хотите создать, должен содержать такое же количество элементов, что и исходный массив. Если вы меняете форму массива из 1 2 элементов, вам необходимо убедить­ ся, что ваш новый массив тоже будет содержать 1 2 элементов.

s_ = np.arange(6)
s_.reshape(3, 2)

# # Добавление оси
#
# Размерность массива можно увеличить с помощью newaxis() и expand_dims().
# Функция newaxis() позволяет увеличить размер вашего массива на одно измерение. Это означает, что одномерный массив станет двумерным, двумерный массив станет трехмерным и т. д.
#
# # Индексирование и срезы
#
# У массивов NumPy есть индексы и срезы, как и у списков Python.
#

c_ = s_[(s_ % 2 == 0) & (s_ > 1)]
c_

# # Создание массива из существующих данных

data = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

ap_ = data[3:8]
ap_

# Соединяем два массива по горизонтали

horizontal = np.hstack((x_, y_))
horizontal

# По вертикали

vertical = np.vstack((x_, y_))
vertical

# Разбиваем массивы на несколько малых

w_ = np.arange(24).reshape(6, 4)
w_

np.vsplit(w_, 3)  # по вертикали

np.hsplit(w_, 2)  # по горизонтали

# # Копии и представления массивов
#
# При работе с массивами данные иногда копируются в новый массив, а иногда нет. Это часто сбивает с толку новичков. Есть три возможных варианта:
#
# 1. Простое присваивание (без копии).
#
# 2. Представление или неглубокая копия.
#
# 3. Копирование или глубокая копия.
#
# **Простое присваивание**
#
# При простом присваивании объекты и их данные не копируются
#
# **Представление или неглубокая копия**
#
# В разных объектах массива могут использоваться одни и те же данные. Метод view() создает новый объект массива, который просматривает те же данные

o_ = x_.view()
o_ is x_

o_.base is x_

o_.reshape(3, 2)  # форма x_ не изменилась

# Срез массива также возвращает его представление

# # Глубокая копия

# Метод ndarray.сору() делает полную копию массива и его данных
#
# Иногда метод сору() следует вызывать после получения среза, если исходный мас­сив больше не нужен. Предположим, что а - это объемный промежуточный мас­сив, а конечный результат b содержит только небольшую часть а. Тогда при по­ строении b необходимо сделать глубокую копию:

b_ = x_[2:].copy()
del x_  # освобождаем память от промежуточного массива
