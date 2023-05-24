def correlation_code(s):
    x = list(s)
    s = ''
    for i in x:
        s += i + str((int(i) + 1) % 2)
    return s


def main():
    amount_codes = int(input('Enter amount of codes: '))
    codes = []
    print('Enter bit array values separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        codes.append(s)

    for element in codes:
        print(element, '=>', correlation_code(element))

    error_codes = []
    print('Enter bit array values with errors separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        error_codes.append(s)

    for element in error_codes:
        error = '-'
        for j in range(0, len(element), 2):
            if (element[j] == '1' and element[j + 1] == '1') or (element[j] == '0' and element[j + 1] == '0'):
                error = '+'
                break
        print(f"Code: {element}\t\t Error: {error}")


if __name__ == '__main__':
    main()
