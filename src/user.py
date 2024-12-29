from aquarium import Aquarium
from typing import Set

class User:
    def __init__(self, name: str, id: int, balance: float):
        self.name = name
        self.id = id
        self.aquariums: Set[Aquarium] = set()
        self.balance = balance

    def __str__(self):
        return f"{self.name} ({self.balance})"

    def add_aquarium(self, aquarium: Aquarium):
        if aquarium in self.aquariums:
            print("Aquarium already exists")
        self.aquariums.add(aquarium)

    def remove_aquarium(self, aquarium: Aquarium):
        if aquarium not in self.aquariums:
            print("Aquarium doesn't exist")
        self.aquariums.discard(aquarium)
