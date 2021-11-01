from abc import abstractmethod, ABC


class WeaponBehavior(ABC):
    @abstractmethod
    def useWeapon(self):
        pass


class BowAndArrowBehavior(WeaponBehavior):

    def useWeapon(self):
        return "USE BOW AND ARROW"


class AxeBehavior(WeaponBehavior):

    def useWeapon(self):
        return "USE AXE"


class KnifeBehavior(WeaponBehavior):

    def useWeapon(self):
        return "USE KNIFE"


class SwordBehavior(WeaponBehavior):

    def useWeapon(self):
        return "USE SWORD"


class Character(ABC):

    def __init__(self, weapon: WeaponBehavior):
        self.weapon = weapon

    @abstractmethod
    def fight(self):
        pass


class Knight(Character):
    def __init__(self, weapon: WeaponBehavior):
        super().__init__(weapon)
        self.weapon = weapon

    def fight(self):
        print(f"KNIGHT FIGHTS with {self.weapon.useWeapon()}")


class King(Character):
    def __init__(self, weapon: WeaponBehavior):
        super().__init__(weapon)
        self.weapon = weapon

    def fight(self):
        print(f"KING FIGHT with {self.weapon.useWeapon()}")


class Troll(Character):
    def __init__(self, weapon: WeaponBehavior):
        super().__init__(weapon)
        self.weapon = weapon

    def fight(self):
        print(f"TROLL FIGHTS with {self.weapon.useWeapon()}")


class Queen(Character):
    def __init__(self, weapon: WeaponBehavior):
        super().__init__(weapon)

    def fight(self):
        print(f"QUEEN FIGHT with {self.weapon.useWeapon()}")


if __name__ == '__main__':
    bosse = Queen(KnifeBehavior())
    bosse.fight()

    goran = Troll(AxeBehavior())
    goran.fight()

    daniel = King(SwordBehavior())
    daniel.fight()

    tommy = Knight(BowAndArrowBehavior())
    tommy.fight()