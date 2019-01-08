"""Using rjust(), ljust(), and center() lets you ensure that strings are neatly aligned, even if you aren’t sure
    how many characters long your strings are."""


def print_picnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnicItems, 12, 5)
print_picnic(picnicItems, 20, 6)
