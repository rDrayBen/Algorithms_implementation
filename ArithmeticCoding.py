from decimal import Decimal, getcontext
from math import log2
from math import ceil


def encode(text, frequencies, precision):
    getcontext().prec = precision
    symbols = list(frequencies.keys())
    global low_point, high_point
    low_point = {symbols[0]: Decimal(0)}
    high_point = {}
    l = 1

    for char in text:
        l *= frequencies[char]

    len_coded_text = ceil(Decimal(log2(Decimal(1/Decimal(l)))))

    for i in range(len(symbols) - 1):
        temp = symbols[i]
        low_point[symbols[i + 1]] = Decimal(low_point[temp] + Decimal(frequencies[temp]))

    for i in range(len(symbols)):
        temp = symbols[i]
        high_point[temp] = Decimal(low_point[temp] + Decimal(frequencies[temp]))

    for key, value in low_point.items():
        print(f'{key}: [{value}; {high_point[key]})')

    print('\n')

    low_range = Decimal(low_point[text[0]])
    high_range = Decimal(high_point[text[0]])
    print(f'Symbol: {text[0]}\tInterval: [{low_range: .{precision}f}; {high_range: .{precision}f})')
    for i in range(1, len(text)):
        size_range = Decimal(high_range - low_range)
        high_range = Decimal(low_range + size_range * high_point[text[i]])
        low_range = Decimal(low_range + size_range * low_point[text[i]])
        print(f'Symbol: {text[i]}\tInterval: [{low_range: .{precision}f}; {high_range: .{precision}f})')
    global code
    code = Decimal((high_range + low_range) / 2)
    print(f'Result point is ({high_range: .{precision}f} + {low_range: .{precision}f}) / 2 = {code: .{precision}f}')
    print(f'Coded message len: {len_coded_text}')
    print(f'Bit input message len: {len(text)*8}')


def decode(encoded_message, symbol_probabilities, text_len):
    message = ""
    while encoded_message < 1:
        for key, value in symbol_probabilities.items():
            if low_point[key] <= encoded_message < high_point[key]:
                message += key
                if len(message) == text_len:
                    print(f'Current message: {message}\tCurrent value of encoded message: {encoded_message}\t'
                          f'Interval: [{low_point[key]}; {high_point[key]})')
                    return message
                print(f'Current message: {message}\tCurrent value of encoded message: {encoded_message}\t'
                      f'Interval: [{low_point[key]}; {high_point[key]})')
                encoded_message = (encoded_message - low_point[key]) / (high_point[key] - low_point[key])
                break
    return message


def main():
    input_string = 'abghibceea'
    freq = {
        'a': 0.11,
        'b': 0.14,
        'c': 0.1,
        'd': 0.15,
        'e': 0.07,
        'f': 0.1,
        'g': 0.1,
        'h': 0.04,
        'i': 0.09,
        'j': 0.1
            }

    precis = len(input_string) + int(len(input_string) * 0.2)
    encode(text=input_string, frequencies=freq, precision=precis)
    print('\n')
    decode(code, freq, len(input_string))


if __name__ == '__main__':
    main()
