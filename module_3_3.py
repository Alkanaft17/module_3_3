def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов
print_params(1, 2, 4)
print_params(78, None)
print_params([6, False, 'Str'])
print_params(*[6, False, 'Str'])
print_params(a=7)
print_params(a='one', c=False)
print_params()

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])

# Создайте список values_list с тремя элементами разных типов.
values_list: list = [True, 'Rock', 5]

# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict: dict = {'a': 45, 'b': True, 'c': 'Start'}

# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)

# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [4.5, 'Stop']

# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2)

#Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
#В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
#def a(my_list = [])) – это приводит к ошибкам!
#Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
    print(item, list_my)
append_to_list(1)
