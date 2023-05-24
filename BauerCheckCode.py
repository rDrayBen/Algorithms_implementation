def bauer_code(s):
    n = s.count('1')
    if n % 2 == 0:
        return s * 2
    else:
        return s + ''.join([str((int(i) + 1) % 2) for i in list(s)])


def main():
    amount_codes = int(input('Enter amount of codes: '))
    codes = []
    print('Enter bit array values separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        codes.append(s)

    for element in codes:
        res_code = bauer_code(element)
        print(element, '=>', res_code)

    error_codes = []
    print('Enter bit array values with errors separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        error_codes.append(s)

    for i in range(len(error_codes)):
        n = error_codes[i][:len(codes[i])].count('1')
        if n % 2 == 0:
            if error_codes[i][:len(codes[i])] == error_codes[i][len(codes[i]):]:
                print(f"Code: {error_codes[i]}\t\t Error: -")
            else:
                print(f"Code: {error_codes[i]}\t\t Error: +")
        else:
            new_error_code = error_codes[i][:len(codes[i])] + \
                             ''.join([str((int(i) + 1) % 2) for i in list(error_codes[i][len(codes[i]):])])
            if new_error_code[:len(codes[i])] == new_error_code[len(codes[i]):]:
                print(f"Code: {error_codes[i]}\t\t Error: -")
            else:
                print(f"Code: {error_codes[i]}\t\t Error: +")


if __name__ == '__main__':
    main()
