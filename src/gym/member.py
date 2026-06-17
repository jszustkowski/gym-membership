"""Klasa reprezentująca członka siłowni."""


class Member:
    """Członek siłowni."""

    def __init__(
        self,
        member_id: int,
        first_name: str,
        last_name: str,
        email: str,
        age: int,
    ) -> None:
        """Tworzy nowego członka.

        Zgłasza ValueError, jeśli e-mail nie zawiera znaku '@'.
        """
        if "@" not in email:
            raise ValueError("Nieprawidłowy adres e-mail.")
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def full_name(self) -> str:
        """Zwraca imię i nazwisko członka."""
        return f"{self.first_name} {self.last_name}"

    def is_adult(self) -> bool:
        """Sprawdza, czy członek jest pełnoletni."""
        return self.age >= 18
