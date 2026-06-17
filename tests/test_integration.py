"""Testy integracyjne — sprawdzają współdziałanie wielu klas naraz."""

import pytest

from gym import FitnessClass, Gym, Member, Membership, Payment, Trainer


def test_full_flow():
    """Pełna ścieżka: członek -> karnet -> płatność -> zajęcia."""
    gym = Gym("FitZone")

    anna = Member(1, "Anna", "Kowalska", "anna@example.com", 25)
    gym.add_member(anna)

    membership = Membership(anna, "Standard", 120.0, 30)
    gym.register_payment(Payment(anna, membership.price))

    trainer = Trainer(1, "Marek", "joga")
    joga = FitnessClass("Joga poranna", trainer, 5)
    gym.add_class(joga)
    joga.add_member(anna)

    assert gym.member_count() == 1
    assert gym.total_income() == 120.0
    assert joga.free_spots() == 4
    assert membership.is_active() is True


def test_class_fills_up():
    """Kilku członków zapisuje się na zajęcia aż do wyczerpania miejsc."""
    gym = Gym("FitZone")
    trainer = Trainer(1, "Marek", "spinning")
    spinning = FitnessClass("Spinning", trainer, 2)
    gym.add_class(spinning)

    members = []
    for i in range(3):
        m = Member(i, f"Imie{i}", f"Nazwisko{i}", f"u{i}@example.com", 30)
        gym.add_member(m)
        members.append(m)

    spinning.add_member(members[0])
    spinning.add_member(members[1])

    assert spinning.is_full() is True
    with pytest.raises(ValueError):
        spinning.add_member(members[2])


def test_income_from_many_members():
    """Wielu członków płaci za karnety, liczymy łączny przychód."""
    gym = Gym("FitZone")
    total = 0.0
    for i in range(4):
        m = Member(i, f"Imie{i}", f"Nazwisko{i}", f"u{i}@example.com", 30)
        gym.add_member(m)
        gym.register_payment(Payment(m, 100.0))
        total += 100.0

    assert gym.member_count() == 4
    assert gym.total_income() == total
