"""Testy klasy Gym."""

from gym import FitnessClass, Gym, Member, Payment, Trainer


def make_member(member_id=1):
    return Member(member_id, "Anna", "Kowalska", "anna@example.com", 25)


def test_add_member_increases_count():
    gym = Gym("FitZone")
    gym.add_member(make_member(1))
    gym.add_member(make_member(2))
    assert gym.member_count() == 2


def test_total_income():
    gym = Gym("FitZone")
    gym.register_payment(Payment(make_member(1), 100.0))
    gym.register_payment(Payment(make_member(2), 50.0))
    assert gym.total_income() == 150.0


def test_add_class():
    gym = Gym("FitZone")
    trainer = Trainer(1, "Marek", "joga")
    gym.add_class(FitnessClass("Joga", trainer, 10))
    assert len(gym.classes) == 1

def test_average_payment():
    gym = Gym("FitZone")
    gym.register_payment(Payment(make_member(1), 100.0))
    gym.register_payment(Payment(make_member(2), 200.0))
    assert gym.average_payment() == 150.0


def test_average_payment_empty():
    gym = Gym("FitZone")
    assert gym.average_payment() == 0.0
