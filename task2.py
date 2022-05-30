# 1.	Найти сумму чисел списка стоящих на нечетной позицииПример:[1,2,3,4] -> 4
'''
import math
import random

def Fill_list(Number_list, Size_list, maximum):

    for i in range(0, Size_list):
        Number_list.append(random.randint(0, maximum+1))
    return Number_list


def Sum_not_even_element(Number_list):
    sum = 0
    for i in range(0, len(Number_list)):
        if i % 2 != 0:
            sum+=Number_list[i]
    return sum


Number_list = []
size = int(input('Введите размер массива: '))
maximum_of_list = int(input('Введите максимальное число в массиве: '))
print(Fill_list(Number_list, size,maximum_of_list))
print(f'Сумма елеметов стояших на нечетной позиции = {Sum_not_even_element(Number_list)}')
'''

# 2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
'''
import random

def Fill_list(numbers_list, size, maximum):
    for i in range(0, size):
        numbers_list.append(random.randint(0, maximum+1))
    return numbers_list


def Product__of_pairs_of_elements(numbers_list):
    result = []
    if len(numbers_list)%2 == 0:
        for i in range(0, len(numbers_list)//2):
            result.append(numbers_list[i]*numbers_list[len(numbers_list)-1-i])
    else:
        for i in range(0, len(numbers_list)//2+1):
            result.append(numbers_list[i]*numbers_list[len(numbers_list)-1-i])


    return result


numbers_list = []
size = int(input('Введите размер массива: '))
maximum_of_list = int(input('Введите максимальное число в массиве: '))
print(Fill_list(numbers_list, size, maximum_of_list))
print(Product__of_pairs_of_elements(numbers_list))
'''


# 3.	В заданном списке вещественных чисел найдите разницу между максимальным
#  и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
def Finding_Max_Min(result_list):
    max_element = max(result_list)                  # нашел не понятную странность когда прописывал в ручную поиск MAX и MIN
    min_element = min(result_list)                  # то максимальное искалось норм а минимальное было равно 0
    Max_min = (max_element,min_element )            # при том что даже удалял его из списка ну этот 0 
    return Max_min                                  # но он все равно его как то находил не понятно откуда, 
                                                    # А библиотечные функции MAX и MIN работают исправно 
def Remove_0(result_list, Max_Min):
    result_list.remove(Max_Min[1])
    return result_list



float_list_numbers = [1.1, 1.2, 3.1, 5, 10.01]
result_list = []
for i in range(0, len(float_list_numbers)):
    result_list.append(float_list_numbers[i]-int(float_list_numbers[i]))
#print(result_list)
Max_Min = Finding_Max_Min(result_list)
#print(Max_Min)
print(Remove_0(result_list, Max_Min))
result_Max_Min = Finding_Max_Min(result_list)
#print(result_Max_Min)
Difference = result_Max_Min[0]-result_Max_Min[1]
print(round(Difference, 3))
'''

# 4.	Написать программу преобразования десятичного числа в двоичное

'''
def Transfer_from_system_10_to_system_2(numb):
    number_in_system_2 = []
    numb1 = numb
    remainder = 0
    i = 0
    while numb1 >= 2:
        remainder = numb1 % 2
        number_in_system_2.append(remainder)
        numb1 //= 2
        i += 1
    number_in_system_2.append(numb1)
    return number_in_system_2

def List_flip(number_in_system_2_list):
    for i in range(len(number_in_system_2_list)//2):
        temp = number_in_system_2_list[i]
        number_in_system_2_list[i] = number_in_system_2_list[len(number_in_system_2_list)-1-i]
        number_in_system_2_list[len(number_in_system_2_list)-1-i] = temp
    return number_in_system_2_list

number = int(input("Enter number: "))
number_in_system_2_list = Transfer_from_system_10_to_system_2(number)
List_flip(number_in_system_2_list)
print(f'Число {number} в 2-ой системе {number_in_system_2_list}')
'''
