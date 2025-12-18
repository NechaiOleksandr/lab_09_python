class Apple:
    states = {0: "Відсутнє", 1: "Цвітіння", 2: "Зелене", 3: "Червоне"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class AppleTree:
    def __init__(self, count):
        self.apples = [Apple(i) for i in range(1, count + 1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []


class Gardener:
    def __init__(self, name, tree):
        self.name = name
        self._tree = tree

    def work(self):
        print(f"Садівник {self.name} працює в саду...")
        self._tree.grow_all()

    def harvest(self):
        print(f"Садівник {self.name} намагається зібрати врожай...")
        if self._tree.all_are_ripe():
            self._tree.give_away_all()
            print("Урожай успішно зібрано! Тепер дерево порожнє.")
        else:
            print("Попередження: Не всі яблука ще дозріли!")

    @staticmethod
    def apple_base():
        print("Стадії дозрівання яблук:")
        for step, name in Apple.states.items():
            print(f"{step}: {name}")
        print("Урожай можна збирати тільки на стадії 'Червоне' (3).")


Gardener.apple_base()
tree = AppleTree(3)

worker = Gardener("Олександр", tree)
worker.work()
worker.harvest()
worker.work()
worker.work()
worker.harvest()