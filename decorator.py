from datetime import datetime


def my_first_decorator(old_function):
    def new_function (*args, **kwargs):
        with open ('RESULTAT.txt', 'a', encoding = 'utf-8') as file:
            file.write (f'Время запуска функции: {datetime.now()}\n')
            file.write (f'Название функции: {old_function.__name__}\n')
            file.write (f'Аргументы функции: {args} и {kwargs}\n')
            result = old_function(*args, **kwargs)
            file.write (f'Результат работы функции: {result}\n\n')
            print (f'Запись данных работы функции {old_function.__name__} произведена')
        return result
    return new_function

def my_second_decorator(path):
    def my_decorator(old_function):
        def new_function (*args, **kwargs):
            with open (path, 'a', encoding = 'utf-8') as file:
                file.write (f'Время запуска функции: {datetime.now()}\n')
                file.write (f'Название функции: {old_function.__name__}\n')
                file.write (f'Аргументы функции: {args} и {kwargs}\n')
                result = old_function(*args, **kwargs)
                file.write (f'Результат работы функции: {result}\n\n')
                print (f'Запись данных работы функции {old_function.__name__} произведена')
            return result
        return new_function
    return my_decorator
