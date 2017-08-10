def padding(num):
    pad_num = num
    r = 3 - len(num) % 3
    if len(num) % 3 != 0:
        pad_num = num.zfill(len(num) + r)
    return pad_num


def break_parts(num):
    num_list = [num[i:i+3] for i in range(0, len(num), 3)]
    return num_list


def naming_block(num):
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    word = ''

    if a > 0:
        word += ones[a] + ' hundred '
    if b > 1:
        word += tens[b] + '-' + ones[c] + ' '
    elif b == 1:
        word += teens[c]
    else:
        word += ones[c]
    return word.strip()


def number_to_words(number_string):
    i, d = number_string.split('.')
    print(i, d)
    pad_i = padding(i)
    num_parts = break_parts(pad_i)
    print(num_parts)

    for i in num_parts:
        print(naming_block(i))

    words = [naming_block(i) for i in num_parts]

    phrase = ','.join(words)
    return phrase
    

ones = {0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}

teens = {0: 'ten',
         1: 'eleven',
         2: 'twelve',
         3: 'thirteen',
         4: 'fourteen',
         5: 'fifteen',
         6: 'sixteen',
         7: 'seventeen',
         8: 'eighteen',
         9: 'nineteen'}

tens = {2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'}


if __name__ == '__main__':
##    number_string = '1234567411.79'
    number_string = '1234000411.79'
    print(number_to_words(number_string))
