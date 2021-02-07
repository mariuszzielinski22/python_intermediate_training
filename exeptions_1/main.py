from exeptions_1.excersises import case_1, case_2, case_3, case_4, case_4_v_2


def main():
    print('Start up')

    # try:
    #     case_2('')
    # except ValueError as ve:
    #     print(f'{ve.args} returned')

    # result = case_3(10, 0)
    # print(result)
    # print(f'Finish')

    dictionary = {
        "rzeczy": ['butter', 'bread']
    }
    case_4_v_2(dictionary)


if __name__ == '__main__':
    main()
