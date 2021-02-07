import sys

def case_1():
    # given
    list_of_numbers = [1, 5, 8, 10, 21]
    # when
    print('Case_1 before')
    # then; wersja pierwsza
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'Exception couht {ie.args}')
    except Exception as exp:
        print(f'Exception cought {exp.args}')

    print('Case_1 after')

    # then; wersja druga
    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'Exception cought by touple {e.args}')


def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty.')
    print(f"Given name is: {name}")


def case_3(number: int, divisor: int) -> float:
    result = 0
    try:
        result = number / divisor
    except ZeroDivisionError as zde:
        print(f'Nie dziel przez zero')
        result = sys.float_info.max
        # result = float(sys.maxsize)
    return result

def case_4(dictionary: dict):
    key = 'items'
    try:
        items: list = dictionary[key]
        for item in items:
            print(item)
    except KeyError as key_error:
        print(f'Key {key} not found, more information{key_error.args}')

def case_4_v_2(dictionary: dict):
    key = 'items'
    items: list = dictionary.get(key, [])
    for item in items:
        print(item)
    if not items:
        print(f'Key does not exist or list is empty')
