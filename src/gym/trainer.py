"""Klasa reprezentująca trenera siłowni."""


class Trainer:
    """Trener prowadzący zajęcia."""

    def __init__(self, trainer_id: int, name: str, specialty: str) -> None:
        """Tworzy trenera o danej specjalizacji (np. 'joga')."""
        self.trainer_id = trainer_id
        self.name = name
        self.specialty = specialty

    def describe(self) -> str:
        """Zwraca krótki opis trenera."""
        return f"{self.name} ({self.specialty})"
