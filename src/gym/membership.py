"""Klasa reprezentująca karnet członka siłowni."""

from gym.member import Member


class Membership:
    """Karnet wykupiony przez członka."""

    def __init__(
        self, member: Member, plan_name: str, price: float, days: int
    ) -> None:
        """Tworzy karnet.

        Zgłasza ValueError, jeśli cena jest ujemna.
        """
        if price < 0:
            raise ValueError("Cena nie może być ujemna.")
        self.member = member
        self.plan_name = plan_name
        self.price = price
        self.days = days
        self.active = True

    def is_active(self) -> bool:
        """Sprawdza, czy karnet jest aktywny."""
        return self.active

    def deactivate(self) -> None:
        """Dezaktywuje karnet (np. po wygaśnięciu lub rezygnacji)."""
        self.active = False

    def describe(self) -> str:
        """Zwraca krótki opis karnetu."""
        status = "aktywny" if self.active else "nieaktywny"
        return f"{self.plan_name} ({self.price} zl, {self.days} dni) - {status}"
