"""objet unite"""

from random import randint


class Unite:
    """
    A class representing a unit in the game.

    Attributes
    ----------
    name : str
        The name of the unit.
    classe : str
        The class of the unit.
    max_health : int
        The maximum health of the unit.
    health : int
        The current health of the unit.
    armor : int
        The armor of the unit.
    speed : int
        The speed of the unit.
    range : int
        The range of the unit.
    ammo : str
    """

    def __init__(self, infolist: list[str]):

        self.name = infolist[0]
        self.classe = infolist[1]

        self.max_health = int(infolist[2])
        self.health = self.max_health
        self.armor = int(infolist[3])

        self.speed = int(infolist[4])
        self.range = int(infolist[5])

        self.ammo = infolist[6]
        self.base_damage = int(infolist[7])
        self.base_penetration = int(infolist[8])

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"""
        Unite {self.name}
        {self.health}/{self.max_health}
        {self.armor}
        {self.speed}
        {self.range}
        {self.ammo}
        {self.base_damage}/{self.base_penetration}
        """

    def __random_penetration(self):
        return randint(-5, 11)

    def __random_damage(self):
        return randint(-10, 26)

    def __damage_calc(self, target: object, pen_factor: float, damage_factor: float):
        """
        Calculate and apply the damage to a target unit based on penetration and damage factors.

        Parameters
        ----------
        target : object
            The target unit object that will receive the damage.
        pen_factor : float
            A multiplier for the base penetration, affecting the chance of penetrating the target's armor.
        damage_factor : float   
            A multiplier for the base damage, affecting the amount of damage applied to the target.

        Notes
        -----
        - If the target's armor is less than or equal to the calculated total penetration,
          full damage is applied.
        - If the target's armor is greater, only a quarter of the calculated damage is applied.
        - Random factors are added to both penetration and damage calculations to introduce variability.
        """

        total_pen = (self.base_penetration + self.__random_penetration()) * pen_factor
        total_damage = (self.base_damage + self.__random_damage()) * damage_factor

        print(total_pen)

        if target.armor <= total_pen:
            target.health -= total_damage
        else:
            target.health -= total_damage / 4

    def shoot(self, target: object, ammo):
        """
        Simulates a shoot from the unite self to the target unite.

        Parameters
        ----------
        target : Unite
            The unite to shoot.
        ammo : str
            The type of ammo to use.

        Notes
        -----
        The damage calculation is done with the following formula:
        target.health -= (self.base_damage + self.__random_damage()) * damage_factor
        if target.armor <= (self.base_penetration + self.__random_penetration()) * pen_factor
        else:
        target.health -= ((self.base_damage + self.__random_damage()) * damage_factor) / 4

        The factors are as follows:
        - HE: pen_factor = 0.5, damage_factor = 2
        - AP: pen_factor = 1, damage_factor = 1
        - HEAT: pen_factor = 1.5, damage_factor = 0.75
        - APCR: pen_factor = 2, damage_factor = 0.5
        """
        if ammo == "HE":
            self.__damage_calc(target, 0.5, 2)

        elif ammo == "AP":
            self.__damage_calc(target, 1, 1)

        elif ammo == "HEAT":
            self.__damage_calc(target, 1.5, 0.75)

        elif ammo == "APCR":
            self.__damage_calc(target, 2, 0.5)


if __name__ == "__main__":
    # tank1 = Unite(unitvar.M24)
    # print(repr(tank1))
    # tank2 = Unite(unitvar.T_50)
    # print(repr(tank2))

    # tank1.shoot(tank2, "APCR")
    # print(repr(tank2))
    pass
