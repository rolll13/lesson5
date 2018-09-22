# Task1
import random


def game(n, k):
    random_num = random.randint(1, n)
    for i in range(k):
        try:
            num = int(input("Введите число: "))
        except (ValueError, UnboundLocalError):
            print("Это не число, -1 попытка")
        else:
            if num == random_num:
                print("Вы угадали")
                break
            elif num <= random_num:
                print("Число должно быть больше")
            else:
                print("Число должно быть меньше")
    print("Попытки кончились")


# Task2
def unic_list_elements(some_list):
    return len(set(some_list))


# Task3
def formating_text(sentence):
    sentence = ' '.join(sentence.title().strip().split())
    return sentence


# Task4
def decorator(str1, str2):
    def inner(i_func):
        def in_inner(*args, **kwargs):
            print(str1)
            print(i_func(*args, **kwargs))
            print(str2)
        return in_inner
    return inner


@decorator('Делай раз', 'Делай два')
def undecorated_func(u_func):
    return u_func
