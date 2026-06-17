"""Przykład użycia systemu siłowni.

Uruchomienie:  python demo.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from gym import FitnessClass, Gym, Member, Membership, Payment, Trainer


def main() -> None:
    """Prezentuje działanie systemu."""
    gym = Gym("FitZone")

    # Członkowie
    anna = Member(1, "Anna", "Kowalska", "anna@example.com", 25)
    jan = Member(2, "Jan", "Nowak", "jan@example.com", 30)
    gym.add_member(anna)
    gym.add_member(jan)

    # Karnety i płatności
    karnet = Membership(anna, "Standard", 120.0, 30)
    gym.register_payment(Payment(anna, karnet.price))
    gym.register_payment(Payment(jan, 120.0))

    # Trener i zajęcia
    trener = Trainer(1, "Marek Zieliński", "joga")
    joga = FitnessClass("Joga poranna", trener, 5)
    gym.add_class(joga)
    joga.add_member(anna)
    joga.add_member(jan)

    # Raport
    print(f"Siłownia: {gym.name}")
    print(f"Liczba członków: {gym.member_count()}")
    print(f"Trener: {trener.describe()}")
    print(f"Zajęcia '{joga.name}' - wolne miejsca: {joga.free_spots()}")
    print(f"Łączny przychód: {gym.total_income()} zł")


if __name__ == "__main__":
    main()
