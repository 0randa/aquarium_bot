from classes.aquarium import Aquarium


class Fish:
    VALID_FISH = {"Guppy", "Neon Tetra", "Molly", "Platy"}

    def __init__(self, species: str, gender: str, months: int):
        """
        Initialises fish instance with species gender and age in months

        Attributes:
            species: str
                the species of the fish
            gender: string
                gender of the fish
            age: int
                age of the person
            hp: int
                hp of a fish

        Methods
        ------
        TODO: add methods later
        """
        self.species = species
        self.gender = gender
        self.age = months
        self.hunger: int = 10
        self.hp: float = 100
        self.survivability = 100
        self.lifespan = 2 * Aquarium.YEAR
        self.alive: bool = True

    def judgement(self, aquarium: Aquarium):
            # check water quality
            self.age += 1

            if 50 <= aquarium.water_quality < 70:
                self.hp -= 0.5
            elif aquarium.water_quality < 50:
                self.hp -= 1

            # check hunger
            if 5 <= self.hunger <= 7:
                self.hp -= 0.5
            elif 0 < self.hunger < 5:
                self.hp -= 1
            elif self.hunger == 0:
                # self is starving, add death penalty to the self
                self.survivability -= 0.33

            self.age = (self.age / self.lifespan) * 100

            if 50 <= self.age < 60:
                self.survivability -= 0.02
            elif 60 <= self.age < 70:
                self.survivability -= 0.03
            elif 70 <= self.age < 80:
                self.survivability -= 0.04
            elif 80 <= self.age < 90:
                self.survivability -= 0.05
            elif 90 <= self.age < 100:
                self.survivability -= 0.06
            elif self.age > 100:
                self.survivability -= 0.10

    def __str__(self):
        return (
            f"specie: {self.species} gender: {self.gender} age (in months): {self.age} "
        )
