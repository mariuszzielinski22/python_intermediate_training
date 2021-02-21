# def file_reader():
#     try:
#         with open("./lorem_ipsum.txt", "r") as read_handler:
#             line_part = read_handler.readline(1024)
#             yield line_part
#
#     except(IOError, Exception) as e:
#         print(f"Problem with reading from file. More info {e.args}")


def file_reader():
    read_handler = open("./lorem_ipsum.txt")
    line_part = read_handler.readline(1024)
    yield line_part