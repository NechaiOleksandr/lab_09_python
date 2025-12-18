class House:
    def __init__(self, area = 50, price = 50000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final = self._price * (100 - discount) / 100
        return final


class SmallHouse(House):
    def __init__(self, price = 40000):
        super().__init__(area = 40, price = price)


class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name = default_name, age = default_age, money = 0, house = None):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Гроші: {self.__money}")
        print(f"Будинок: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        print("Операція успішна: Будинок придбано!")

    def earn_money(self, amount):
        self.__money += amount
        print(f"Зароблено {amount} грошей. Поточний баланс: {self.__money}")

    def buy_house(self, house, discount=10):
        price = house.final_price(discount)

        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print(f"Увага! Недостатньо коштів. Потрібно {price}, а є {self.__money}")


Human.default_info()
human = Human(name = "Олександр", age = 30, money = 10000)
human.info()
small_house = SmallHouse(price = 8000)
print(f"Ціна будинку (без знижки): {small_house._price}")
expensive_house = SmallHouse(price = 50000)
human.buy_house(expensive_house)
human.earn_money(40000)
human.buy_house(expensive_house)
human.info()