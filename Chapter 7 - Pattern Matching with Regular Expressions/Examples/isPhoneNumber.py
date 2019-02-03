def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def check_for_numbers(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')

if __name__ == '__main__':
    a = '413-436-6654'
    b = 'yol-osw-ag12'
    c = '123456789123'
    print(isPhoneNumber(a))
    print(isPhoneNumber(b))
    print(isPhoneNumber(c))