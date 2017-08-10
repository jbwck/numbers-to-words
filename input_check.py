from re import match


def check_format(number):
    result = None
    formats = {'^\d+?$': '%%%.00',
               '^\d+?\.$': '%%%00',
               '^\d+?\.\d$': '%%%0',
               '^\d+?\.\d\d$': '%%%',
               '^$': '0.00',
               '^\.$': '0.00',
               '^\.\d$': '0%%%0',
               '^\.\d\d$': '0%%%'}

    try:
        # Returns properly formatted number or None if input number is invalid
        # format
        num = number.replace(',', '')
        for pattern, value in formats.items():
            if hasattr(match(pattern, num), 'group'):
                result = value.replace('%%%', num)
                break

    except:
        # return False if input data type is not string
        result = False

    return result


if __name__ == '__main__':
    test_input = ['$0', '1234', '1234.', '1234.5', '1234.56', '1,903,447.99',
                  '', '.7', '.78', '23a.34', '1,234.11', True, False, '123.E4',
                  'NaN', '.454', eval('45')]
    
    for i in test_input:
        ws = 12 - len(str(i))
        print(i, ' ' * ws, "  -->  ", check_format(i))
