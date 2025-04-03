import random
import numpy as np

# Задача 1: Заполнить массив случайными числами и найти наибольший элемент и его индекс.
def task1():
    array = [random.randint(1, 100) for _ in range(10)]
    max_element = max(array)
    max_index = array.index(max_element)
    print("Array:", array)
    print("Max Element:", max_element, "at Index:", max_index)

# Задача 2: Сумма чётных положительных элементов массива.
def task2():
    array = [random.randint(-50, 50) for _ in range(10)]
    even_positive_sum = sum(x for x in array if x > 0 and x % 2 == 0)
    print("Array:", array)
    print("Sum of Even Positive Elements:", even_positive_sum)

# Задача 3: Найти элементы, меньше среднего арифметического.
def task3():
    array = [random.randint(1, 100) for _ in range(10)]
    avg = sum(array) / len(array)
    less_than_avg = [x for x in array if x < avg]
    print("Array:", array)
    print("Average:", avg)
    print("Elements less than average:", less_than_avg)

# Задача 4: Найти два наименьших элемента массива.
def task4():
    array = [random.randint(1, 100) for _ in range(10)]
    first_min, second_min = sorted(array)[:2]
    print("Array:", array)
    print("Two Smallest Elements:", first_min, second_min)

# Задача 5: Найти сумму всех цифр массива.
def task5():
    array = [random.randint(10, 1000) for _ in range(10)]
    digit_sum = sum(int(digit) for num in array for digit in str(abs(num)))
    print("Array:", array)
    print("Sum of All Digits:", digit_sum)

# Задача 6: Среднее арифметическое положительных элементов массива.
def task6():
    array = [random.randint(-50, 50) for _ in range(10)]
    positive_elements = [x for x in array if x > 0]
    avg_positive = sum(positive_elements) / len(positive_elements) if positive_elements else 0
    print("Array:", array)
    print("Average of Positive Elements:", avg_positive)

# Задача 7: Поменять местами минимальный и максимальный элементы массива.
def task7():
    array = [random.randint(1, 100) for _ in range(10)]
    min_index, max_index = array.index(min(array)), array.index(max(array))
    array[min_index], array[max_index] = array[max_index], array[min_index]
    print("Modified Array:", array)

# Задача 8: Найти сумму, произведение и среднее арифметическое элементов матрицы.
def task8():
    matrix = np.random.randint(1, 10, (3, 3))
    total_sum = matrix.sum()
    total_product = np.prod(matrix)
    avg = matrix.mean()
    print("Matrix:\n", matrix)
    print("Sum:", total_sum, "Product:", total_product, "Average:", avg)

# Задача 9: Найти сумму элементов главной диагонали матрицы.
def task9():
    matrix = np.random.randint(1, 10, (3, 3))
    diagonal_sum = np.trace(matrix)
    print("Matrix:\n", matrix)
    print("Sum of Main Diagonal:", diagonal_sum)

# Выполнение задач
if __name__ == "__main__":
    print("Task 1")
    task1()
    print("\nTask 2")
    task2()
    print("\nTask 3")
    task3()
    print("\nTask 4")
    task4()
    print("\nTask 5")
    task5()
    print("\nTask 6")
    task6()
    print("\nTask 7")
    task7()
    print("\nTask 8")
    task8()
    print("\nTask 9")
    task9()
