def make_dictionary(x: str):
    s_dict = dict()
    s_dict['null'] = 0
    i = 0
    index = 1
    phrase = ''
    while i < len(x):
        phrase += x[i]
        if phrase not in s_dict:
            s_dict[phrase] = index
            index += 1
            phrase = ''
        i += 1
    if phrase != '':
        phrase += '(eof)'
        s_dict[phrase] = index

    print('\nDictionary: ')
    for key, value in s_dict.items():
        print(value, '  ', key)
    return s_dict


def make_marks(s_dict: dict):
    marks_list = list()
    for key, value in s_dict.items():
        temp = list()
        if key == 'null':
            continue
        elif len(key) == 1:
            temp.append(key)
            temp.append(0)
            marks_list.append(temp)
        elif '(eof)' in key:
            temp.append('(eof)')
            temp.append(s_dict[key[:-5]])
            marks_list.append(temp)
        elif len(key) > 1:
            temp.append(key[-1:])
            temp.append(s_dict[key[:-1]])
            marks_list.append(temp)
    print('Code phrases: ')
    print('\n'.join(f'{index}  {char}' for char, index in marks_list))
    print('Coded string: ')
    print(' '.join(f'{index}{char}' for char, index in marks_list))

    avg_len = sum(len(str(index)) + len(char) for char, index in marks_list)
    print('Average coded phrase length: ', float(avg_len / len(marks_list)))
    print('Coded dict len:', len(s_dict))


def main():
    letters = input("Enter the string: ")

    symbols_dictionary = make_dictionary(letters)

    make_marks(symbols_dictionary)

    print('Input string len:', len(letters))


if __name__ == '__main__':
    main()
