from generators.exercise3 import Iterable


def iterator_ex_1():
    dictionary = {
        'a': 1,
        'b': 2,
        'c': 3
    }

    for key in dictionary.keys():
        print(key)

    for value in dictionary.values():
        print(value)


def number_creator(n):
    list_of_numbers = []
    for number in range(n):
        list_of_numbers.append(number)
    return list_of_numbers


def iterator_ex_2(n):
    print('exercise2')
    import sys
    result_list = number_creator(n)
    print(f'Size of list in bytes: {sys.getsizeof(result_list)}')
    result = sum(result_list)
    print(f'size one umber in bytes: {sys.getsizeof(result)}')
    print(result)


def iterator_ex_3(n):
    print('exercise3')
    import sys
    iterator = Iterable(n)
    print(f'Size of iterator in bytes: {sys.getsizeof(iterator)}')
    result = sum(iterator)
    print(f'size one umber in bytes: {sys.getsizeof(result)}')
    print(result)


def main():
    # iterator_ex_1()
    print("Exercise 2")
    iterator_ex_2(100000)
    print("Exercise 3")
    iterator_ex_3(100000)


if __name__ == '__main__':
    main()
