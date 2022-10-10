class Item:

    def __init__(self, name, price, decription, demensions):
        self.price = price
        self.decription = decription
        self.demensions = demensions
        self.name = name

    def __str__(self):
        return f'Item: {self.name}, {self.price}, {self.decription}, {self.demensions}'


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'User: {self.name}, {self.surname}, {self.numberphone}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        tmp = ''
        for item, cn in self.products.items():
            tmp += f'{str(item.name)}: {cn} pcs. \n'
        return f'User: {self.user.name} {self.user.surname}\n' \
               f'Items:  \n{tmp}'

    def get_total(self):
        total = 0
        for key, cnt in self.products.items():
            total += key.price * cnt
        return total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
rice = Item('rice', 5, 'white', "big")
buyer = User("Ivan", "Ivanov", "02628162")
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print(cart.get_total())

