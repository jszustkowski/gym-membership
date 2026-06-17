"""Klasa reprezentująca płatność."""

from gym.member import Member


class Payment:
    """Płatność dokonana przez członka."""

    def __init__(self, member: Member, amount: float) -> None:
        """Tworzy płatność.

        Zgłasza ValueError, jeśli kwota nie jest dodatnia.
        """
        if amount <= 0:
            raise ValueError("Kwota musi być dodatnia.")
        self.member = member
        self.amount = amount
        self.paid = False

    def pay(self) -> None:
        """Oznacza płatność jako opłaconą."""
        self.paid = True

    def refund(self) -> None:
        """Cofa opłaconą płatność (zwrot).

        Zgłasza ValueError, jeśli płatność nie była opłacona.
        """
        if not self.paid:
            raise ValueError("Nie można zwrócić nieopłaconej płatności.")
        self.paid = False
