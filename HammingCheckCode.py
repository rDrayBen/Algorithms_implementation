def hamming_encode(data):
    k = len(data)
    r = 1

    while 2 ** r < r + k + 1:
        r += 1

    encoded = [0] * (k + r)
    parity_positions = [2 ** i for i in range(r)]

    j = 0
    for i in range(1, k + r + 1):
        if i in parity_positions:
            continue
        encoded[i-1] = int(data[j])
        j += 1

    for pos in parity_positions:
        ones_count = 0
        for i in range(1, k + r + 1):
            if i & pos:
                ones_count += encoded[i-1]

        encoded[pos-1] = ones_count % 2

    return ''.join(str(el) for el in encoded)


def hamming_decode(received):
    bits = [1 if el == '1' else 0 for el in received]
    n = len(received)
    error_index = 0

    step = 1
    while True:
        need = bits[step - 1]
        for curr in range(step, n + 1, 2 * step):

            for i in range(curr, curr + step):
                if i > n:
                    break
                if i != step:
                    need ^= bits[i - 1]

        if need == 1:
            error_index += step

        step *= 2
        if step > n:
            break

    if error_index != 0:
        bits[error_index - 1] ^= 1

    return ''.join('1' if el == 1 else '0' for el in bits), error_index - 1


def main():
    amount_codes = int(input('Enter amount of codes: '))
    codes = []
    print('Enter bit array values separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        codes.append(s)

    for element in codes:
        print(element, '=>', hamming_encode(element))

    error_codes = []
    print('Enter bit array values with errors separated with enter: ')
    for i in range(amount_codes):
        s = input().strip()
        error_codes.append(s)

    for element in error_codes:
        res, err = hamming_decode(element)
        print(f"Decoded: {res}\t\tError index: {err}")


if __name__ == '__main__':
    while True:
        main()

