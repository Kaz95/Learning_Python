print('imported')


class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def print_name_quantity(self):
        print('{} - {}').format(self.name, self.quantity)

    def add_one(self):
        self.quantity += 1

    def minus_one(self):
        self.quantity -= 1


if __name__ == '__main__':
    i = Item('Arrow', 1)
    print(i.name)
    print(i.quantity)
