class Сlothes:
    def __init__(self, size_suit=0, size_coat=0):
        self.size_suit = size_suit
        self.size_coat = size_coat

    @property
    def coat_fabric(self):
        return round(self.size_coat / 6.5 + 0.5, 3)

    @property
    def suit_fabric(self):
        return 2 * self.size_suit + 0.3


suit = Сlothes(size_suit=10)
print(suit.suit_fabric)
coat = Сlothes(size_coat=10)
print(coat.coat_fabric)
