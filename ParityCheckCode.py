def control_element(s):
    return s + str(s.count('1') % 2)


def main():
    amount_codes = int(input('Enter amount of codes: '))
    codes = []
    print('Enter bit array values separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        codes.append(s)

    print("Coded codes + control symbol: ")
    for i in codes:
        print(i, '=>', control_element(i))

    error_codes = []
    print('Enter bit array values with errors separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        error_codes.append(s)

    for i in range(len(error_codes)):
        print('-' if (error_codes[i].count('1') % 2) == 0 else '+')


if __name__ == '__main__':
    main()

