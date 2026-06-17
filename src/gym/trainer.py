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

    def is_specialist_in(self, specialty: str) -> bool:
        """Sprawdza, czy trener ma daną specjalizację (bez wielkości liter)."""
        return self.specialty.lower() == specialty.lower()
