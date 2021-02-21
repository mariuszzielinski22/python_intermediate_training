def reader_line_by_line():
    read_file = open("./file_to_read.txt")
    for line in read_file:
        yield line