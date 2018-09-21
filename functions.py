import math

print('abs - модуль числа')
print(abs(-1))
print(abs(-1.0))
print(abs(1 + 2j))  # корень из (1^2 + 2^2)

print(math.fabs(-1))  # всегда возвращает float

print('any, all')
# any - возвращает True, если одна из переменных True
print(any([True, False, False]))
print(any([False, False, False]))

# all -  возвращает True, если все True
print(all([True, True, False]))
print(all([True, True, True]))

print('repr, ascii')
print(repr('Привет'))
print(ascii('Привет'))

print('bin, hex, oct')
print(bin(2))  # двоичная система
print(hex(2))  # 16 система
print(oct(2))  # восмиричная система

print('bool, str, int, float')
a = bin(50)
print(a)
a = int(a, 2)
print(a)
print(str(2), repr(2), str(2) == repr(2))

print(bool([]), bool({}), bool("False"), bool("True"))

print('callable - возвращает True, если объект вызываем')


def foo1():
    pass


foo2 = 2

print(callable(foo1), callable(foo2))
if callable(foo1):
    foo1()
else:
    foo2

print('getattr, setattr, hasattr')
print(hasattr(foo1, 'attr'))
if hasattr(foo1, 'attr'):
    print('HAS ATTR', foo1.attr)
setattr(foo1, 'attr', 3)
if hasattr(foo1, 'attr'):
    print('HAS ATTR', foo1.attr)

print('GETATTR', getattr(foo1, 'attr'), getattr(foo1, 'attr1', 'default'))

# foo1.attr = 3  # setattr(foo1, 'attr', 3)
# foo1.attr1  # getattr(foo1, 'attr1')

print('eval, exec - вызов python кода')
codeblock = """
print("1")
print("2")
"""
print(exec(codeblock))  # выполняет блок кода
print(eval("print('a')"))  # выполняет строка кода


print('dir - список объектов из объекта')
print(dir(math))
print(dir("Hello"))
print(dir(1))

print('help - строка документации у объекта')
print(help(math), help(math.fabs))

print('divmod - целочисленное деление + остаток')
print(divmod(11, 4))
print(divmod(11, 4)[0] == 11 // 4, divmod(11, 4)[1] == 11 % 4)

print('enumerate')
print(list(enumerate('hello', 1)))

print('filter, map, sorted')
a = [1, 2, 3, 4, 5, 6, 7]
list(filter(lambda x: x % 2 == 0, a))  # создаем список из четных элементов

b = ['a', 'b', 'c', 'd']
list(map(lambda x: x.upper() * 2, b))
# переводим элементы к верхнему регистру и удваиваем


c = [{'a': 'B'}, {'a': 'a'}, {'a': 'C'}]
sorted(a, key=lambda x: x['a'].lower())
# сортируем по значению ключа 'a' в алфавитном порядке


# next()
a = map(lambda x: x, range(10000000000000000000000))
print(next(a))
# raise StopIteration когда итерация заверешена

# reversed
print(list(reversed([1, 2, 3])))
