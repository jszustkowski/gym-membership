"""Główna klasa zarządzająca siłownią."""

from gym.fitness_class import FitnessClass
from gym.member import Member
from gym.payment import Payment


class Gym:
    """Siłownia — przechowuje członków, zajęcia i płatności."""

    def __init__(self, name: str) -> None:
        """Tworzy pustą siłownię o podanej nazwie."""
        self.name = name
        self.members: list[Member] = []
        self.classes: list[FitnessClass] = []
        self.payments: list[Payment] = []

    def add_member(self, member: Member) -> None:
        """Dodaje członka do siłowni."""
        self.members.append(member)

    def add_class(self, fitness_class: FitnessClass) -> None:
        """Dodaje zajęcia do grafiku siłowni."""
        self.classes.append(fitness_class)

    def register_payment(self, payment: Payment) -> None:
        """Rejestruje płatność i od razu oznacza ją jako opłaconą."""
        payment.pay()
        self.payments.append(payment)

    def member_count(self) -> int:
        """Zwraca liczbę członków siłowni."""
        return len(self.members)

    def total_income(self) -> float:
        """Zwraca sumę wszystkich opłaconych płatności."""
        return sum(p.amount for p in self.payments if p.paid)

    def average_payment(self) -> float:
        """Zwraca średnią kwotę opłaconych płatności (0 gdy brak płatności)."""
        paid = [p.amount for p in self.payments if p.paid]
        if not paid:
            return 0.0
        return sum(paid) / len(paid)
