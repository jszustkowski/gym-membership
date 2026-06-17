"""Klasa reprezentująca zajęcia grupowe."""

from gym.member import Member
from gym.trainer import Trainer


class FitnessClass:
    """Zajęcia grupowe z ograniczoną liczbą miejsc."""

    def __init__(self, name: str, trainer: Trainer, capacity: int) -> None:
        """Tworzy zajęcia.

        Zgłasza ValueError, jeśli pojemność nie jest dodatnia.
        """
        if capacity <= 0:
            raise ValueError("Pojemność musi być dodatnia.")
        self.name = name
        self.trainer = trainer
        self.capacity = capacity
        self.members: list[Member] = []

    def free_spots(self) -> int:
        """Zwraca liczbę wolnych miejsc."""
        return self.capacity - len(self.members)

    def is_full(self) -> bool:
        """Sprawdza, czy zajęcia są pełne."""
        return self.free_spots() <= 0

    def add_member(self, member: Member) -> None:
        """Zapisuje członka na zajęcia.

        Zgłasza ValueError, gdy brak miejsc lub członek jest już zapisany.
        """
        if self.is_full():
            raise ValueError("Brak wolnych miejsc.")
        if member in self.members:
            raise ValueError("Członek jest już zapisany na te zajęcia.")
        self.members.append(member)

    def remove_member(self, member: Member) -> None:
        """Wypisuje członka z zajęć.

        Zgłasza ValueError, jeśli członek nie był zapisany.
        """
        if member not in self.members:
            raise ValueError("Członek nie jest zapisany na te zajęcia.")
        self.members.remove(member)
