# from decorators.case_2 import read_file


# def main():
#     a, b = print_hello_world(1, 2)
#     print(f'In main: {a} {b}')
#
#
# def wrap_before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print('Before')
#         result = func(*args, **kwargs)
#         print('After')
#         return result
#     return wrapper

# read_file(file_path='./abc')


# @wrap_before_and_after
# def print_hello_world(a, b):
#     print("Hello world!")
#     print(f'{a, b}')
#     return a, b

def main():
    read_file(file_path='./abc')

def check_file_wrapper(func):
    def inner(*args, **kwargs):
        path = ""
        if len(args) > 0:
            print(f'Found args {args}')
            path = args[0]
        elif kwargs.get('file_path', ""):
            print(f'Found kwargs {kwargs.get("file_path")}')
            path = kwargs.get('file_path')
        import os
        if path and os.path.exists(path):
            print('Path exist')
        elif path:
            print('Path doesnt exist but file will be created.')
            from pathlib import Path
            Path(path).touch()
        else:
            print('No arguments')
            import sys
            sys.exit(1)
        return func(*args, **kwargs)

    return inner


@check_file_wrapper
def read_file(file_path: str):
    with open(file_path, 'r') as fd:
        fd.read()


if __name__ == '__main__':
    main()
