from math import log
from math import ceil


def berher_code(s):
    x = list(s)
    buf = ''.join([str((int(i) + 1) % 2)
                   for i in bin(s.count('1'))[2:]])
    return s + ' ' + '1' * (-len(buf) + ceil(log(len(s), 2))) + buf


def main():
    amount_codes = int(input('Enter amount of codes: '))
    codes = []
    print('Enter bit array values separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        codes.append(s)

    for element in codes:
        print(element, '=>', berher_code(element))

    error_codes = []
    print('Enter bit array values with errors separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        error_codes.append(s)

    for element in error_codes:
        s1, s2 = element.split(' ')[0], element.split(' ')[1]
        n = s1.count('1')
        s2_check = ''.join([str((int(i) + 1) % 2) for i in bin(n)[2:]])
        s2_check += '1' * (-len(s2_check) + ceil(log(len(s1), 2))) + s2_check
        if s2_check[-len(s2):] != s2:
            print(f"Code: {element}\t\t Error: +")
        else:
            print(f"Code: {element}\t\t Error: -")


if __name__ == '__main__':
    main()
