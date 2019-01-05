# Lists
birthdays = {'Terrance': 'Apr 14', 'Dad': 'Sep 5', 'Sister': 'May 27'}


def main():
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            b_day = input()
            birthdays[name] = b_day
            print('Birthday database updated')


main()
