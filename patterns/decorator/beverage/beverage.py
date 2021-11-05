from abc import ABC, abstractmethod


class Beverage(ABC):
    description: str

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    beverage: Beverage

    @abstractmethod
    def get_description(self) -> str:
        pass


class Espresso(Beverage):
    description: str

    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    description = "House Blend Coffee"

    def cost(self) -> float:
        return .89


class DarkRoast(Beverage):
    description = "Dark Roast"

    def cost(self) -> float:
        return .99


class Decaf(Beverage):
    description = "Decaf"

    def cost(self) -> float:
        return 1.05


class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + .20


class Soy(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + .15


class Whip(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip."

    def cost(self) -> float:
        return self.beverage.cost() + .10


class SteamedMilk(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Steamed Milk."

    def cost(self) -> float:
        return self.beverage.cost() + .10


if __name__ == '__main__':
    espresso = Espresso()
    print(f"""
        {espresso.get_description()} $ {espresso.cost()}
    """)

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)

    print(f"""
        {beverage2.get_description()} $ {beverage2.cost()}
    """)

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)

    print(f"""
           {beverage3.get_description()} $ {beverage3.cost()}
       """)

