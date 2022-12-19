import numpy as np

correct_progression_array = np.arange(1000000, dtype = 'int64')
random_elem_array = np.random.randint(1, 11, 1000000)

#1 задача
print("Сумма ряда [0 - 999999]:")
print(np.sum(correct_progression_array))
print()

#2 задача
print("Среднее значение ряда [0 - 999999]:")
print(np.mean(correct_progression_array, dtype = 'float'))
print()

#3 задача
print("МЕДИАНА случайных чисел ряда из диапазона [1-10] в колличестве - 1000000:")
print(np.median(random_elem_array))
print()

#4 задача
print("ПРОИЗВЕДЕНИЕ случайных чисел ряда из диапазона [1-10] в колличестве - 1000000:")
print(np.prod(random_elem_array, dtype = 'object'))
print()
