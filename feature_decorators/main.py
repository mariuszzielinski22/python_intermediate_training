from functools import wraps


# exercise 3
def catch_io_error_decorator(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IOError as ie:
            print(f"IOError caught {ie.args}")
            return None

    return inner


def catch_io_error_decorator_with_wraps(func):
    @wraps(func)  # zapamietuje sciezke wywołań
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IOError as ie:
            print(f"IOError caught {ie.args}")
            return None

    return inner


@catch_io_error_decorator_with_wraps
def throw_exception_file():
    raise IOError("error shows up")


# exercise 4
@catch_io_error_decorator
def read_not_exist_file():
    with open("./not_exist_file.txt", "r") as fd:
        fd.read()


def main():
    # throw_exception_file()
    read_not_exist_file()


if __name__ == '__main__':
    main()