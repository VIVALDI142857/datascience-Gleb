"""Chapter 1."""

# # Введение в Data Science
# ***Data Science*** - это наука об изучении данных для того, чтобы дан­ные обрели смысл и дали нам полезную информацию. Эта наука не касается какой­ то конкретной предметной области, а являет собой сочетание различных дисцип­лин, связанных с анализом данных и выдаче «умных» результатов и решений, основанных на этих данных.

# <img src="/Users/glebtrofimov/Documents/GitHub/datascience-Gleb/images/img1.png" width="400" height="300"/>
#

#
# # Задачи Data Science
#
# 1. задавать правильные вопросы
# 2. находить основную причину проблемы
# 3. находить закономерности среди, на первый взгляд, хаотичных необработанных данных
# 4. создавать модели для предиктивного анализа
# 5. визуализировать и отображать результаты с помощью графиков, информационных панелей
# 6. наделять машины интеллектом
# 7. определять лояльность клиентов с помощью анализа настроений
# 8. принимать более качественные и быстрые решения
# 9. рекомендовать правильный продукт нужному клиенту для развития бизнеса
#
# # Настоящее и будущее Data Science
#
# ***Искусственныйинтеллект(ИИ)***-это сфера, в которой основное внимание уде­ляется созданию интеллектуальных машин, способных работать и принимать решения как человек.
#
# ***Машинное обучение*** - это инструмент для извлечения знаний из данных.
# В машинном обучении модели могут обучаться на данных самостоятельно или поэтапно: обучение с учителем, т. е. на данных, подготовленных человеком, или обучение без учителя, в котором работа ведется над хаотичными и неорганизо­ванными данными.
#
# ***Глубокое обучение*** - это создание многослойных нейронных сетей в областях, где требуется более продвинутый или быстрый анализ, а традиционное машин­ ное обучение не справляется. Под глубиной понимается наличие более одного скрытого слоя нейронов в сети, которые проводят математические вычисления.
#
# ***Большие данные*** - работа с огромными объемами часто неструктурированных данных. Специфика - инструмены и системы, способные выдерживать высокие нагрузки.
#
# # Чем занимается специалист по Data Science?
#
# ***Специалист по Data Science решает бизнес-задачи с помощью следующих шагов:***
#
# - задает правильные вопросы, чтобы понять проблему
# - собирает данные из нескольких источников - корпоративные данные, общедос­тупные данные
# - обрабатывает сырые данные и преобразует их в формат, подходящий для ана­лиза
# - загружает данные в аналитическую систему - алгоритм машинного обучения или статистическая модель
# - подготавливает результаты и идеи, которые можно изложить заинтересованным сторонам.
#
# ***Специалист решает проблемы:***
# -обнаружение мошенничества и выявление аномалий, например изменений схе­мы снятия или расходования средств с кредитной карты клиента
# - целевой и персонализированный маркетинг - персональные рассылки по элек­тронной почте, системы рекомендаций на сайтах магазинов
# - метрические прогнозы - показатели эффективности, качества рекламных кам­паний и других мероприятий
# - оценка принятия решений - обработка больших объемов данных и помощь в принятии решения, например о выдаче кредита на основе кредитных оценок
# - прогнозирующее моделирование- прогнозирование столкновения метеорита с землей на основе астрономических данных
#
# # Профессии в области DS
# - специалист по данным (манипулирует огромными объемами данных)
# - дата-инженер (работа с большими объемами данных, системами обработки и
# базами данных)
# - аналитик данных (отвечает за сбор огромных объемов данных, поиск в данных отношений, закономерности и тенденций, составление отчестности и визуализацию для анализа данных)
# - статистик (собирает, анализирует, обрабаотывает качественные и количественные данные, используя статистические теории и методы)
# - архитектор данных
# - администратор данных (обеспечивает доступ к базе данных для всех пользователей)
# - бизнес-аналитик (улучшение бизнес-процессов)
# - менеджер данных/аналитики
#
# # Программирование
# **Программирование** - это идеи, преобразованные в пошаговые инструкции
#
# **Алгоритм** - конечная последовательность четко определенных, реализуемых компьютером инструкций для решения какой-либо  проблемы или для выполнения вычислений. Алгоритмы всегда однозначны и используются для вычислений, обработки данных, автоматизированных решений и других задач.
#
# **Блок-схема** - это изображение алгоритмов в графической форме с использованием определенных значений. Для представления различных функций используются некоторые стандартные символы.
#

# <img src="/Users/glebtrofimov/Documents/GitHub/datascience-Gleb/images/BlockScheme.png" width="400" height="300"/>

# # Исходный код
# **Исходный код** - это то, что пишут программисты на всех языках программирова­ния. Это те самые указания, которые мы даем компьютеру, написанные неформа­тированным текстом. В таком тесте нет таких средств форматирования, как выде­ление полужирным, курсив или подчеркивание.
#
# # Как запустить исходный код?
#
# **Три способа перевода исходного кода  в машинный код:**
#
#  - компиляция
#  - интерпретация
#  - сочетание двух этих способов
#
#  Компилятор переводит/ компилирует исходный код с языка программирования высокого уровня на машинный язык. Пример программ: C, C++, Objective C
#
#  **Интерпретатор** - компьютерная программа, которая непосредственно выполняет инструкции, написанные на языке программирования, без предварительной компиляции в программу на машинном языке. Пример программ: PHP, Java Script
#
# # Основные отличия компилятора от интерпретатора
#
#  1. Компилятор генерирует автономную программу, написанную на машинном коде,  а система интерпретатора выполняет действия, описанные программой высокого уровня
#
#  2. После компиляции исходный код для запуска больше не требуется, у интерпретируемых программ исходный код требуется для запуска программы каждый раз
#
# # Интегрированная среда разработки(IDE)
#
# Для решения специфичных задач всегда существует специальное программное обеспечение. Например, когда нужно работать с данными, таблицами и расчетами, мы используем программы для работы с электронными таблицами (например, Microsoft Ехсеl), а если нужна презентация, используем PowerPoint. Для создания или открытия текстовых документов используются текстовые редакторы. Нетрудно предположить, что для написания компьютерных программ существуют интегри­рованные среды разработки или IDE (lntegrated Development Environrnent). В этих программах есть специальные инструменты, необходимые для написания, отладки и компиляции кода.
#
# # Упражнения
#  **1.** Напишите алгоритм для расчета простых процентов от некоторой суммы.
#  Начало функции:
#     ввод данных:
#        сумма = ?     количество требуемых процентов% = ?
#     итог = сумма/100 * количество требуемых процентов%
#     Вывод итога
#
#
# **2.** Алгоритм для вычисления площади прямоугольника
# Начало функции:
#     ввод данных:
#         длина = ?    ширина = ?
#     произведение длины и ширины
#     Возвращение результата
#
#
# **3.** Напишите алгоритм вычисления периметра круга.
# Начало функции:
#     ввод данных:
#        радиус = ?
#     S = 2πr
#     вывод S
#
#
# **4.** Напишите алгоритм, который находит все простые числа меньше 100 (Здесь пишу код чтобы лучше объяснить)
# Начало функции:
#    Ввод:
#        numlist = список всех n | 0 < n <= 100, n ∊ N
#     каждый объект списка numlist проверяем на делимость без остатка на число, меньшее чем оно само.
#
#     Подсчитываем количество делителей, среди которых должны быть только
#     единица и само число (True) else: False
#
#     если True:
#
#         добавляем число в список подходящих
#
#     если False:
#
#         пропускаем число переходим к следующему
#
#     Вывод:
#
#        итоговый список простых чисел
#
#
#
#

# +
# алгоритм, который находит все простые числа меньше 100
# numlist: list[any] = list(range(1, 101))
# total: list[any] = []
# div_list: list[any] = []
# for i in numlist:
#    for divisor in range(1, i + 1):
#        if i % divisor == 0:
#            div_list.append(divisor)
#    if len(div_list) == 2:
#        total.append(i)
#        div_list = []
#    else:
#        div_list = []
#        continue
# total
# -

# **5.** Напишите алгоритм превращения предложения, написанного в верхнем регист­ре, в обычный для предложений регистр.
# Ввод:
#     Предложение в нижнем регистре
#
# Преобразуем все символы в нижний регистр(.lower())
#
# Вывод: Итоговое предложение
#
#
# **6.** Блок-схема для приготовления льда из кипяченой воды с помощью холодильника.

# <img src="/Users/glebtrofimov/Documents/GitHub/datascience-Gleb/images/BlockSchemeWatr.png" width="400" height="300"/>

# **7.** Блок-схема для нахождения суммы всех четных чисел меньше ста.

# <img src="/Users/glebtrofimov/Documents/GitHub/datascience-Gleb/images/chotniyeon1do100.png" width="400" height="300"/>

# **8.** Блок-схема для нахождения суммы всех нечетных чисел от 1 до 15 включительно.

#
# <img src="/Users/glebtrofimov/Documents/GitHub/datascience-Gleb/images/15.png" width="400" height="300"/>

# **9.** Блок-схема вывода таблицы умножения на 3

# <img src="/Users/glebtrofimov/Documents/GitHub/datascience-Gleb/images/x3.png" width="400" height="300"/>

# **10.** Составить блок-схему для расчета сложных процентов с капитализацией

# <img src="/Users/glebtrofimov/Documents/GitHub/datascience-Gleb/images/percentaño.png" width="400" height="300"/>
