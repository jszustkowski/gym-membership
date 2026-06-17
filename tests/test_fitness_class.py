"""Testy klasy FitnessClass."""

import pytest

from gym import FitnessClass, Member, Trainer


def make_trainer():
    return Trainer(1, "Marek Nowak", "joga")


def make_member(member_id=1):
    return Member(member_id, "Anna", "Kowalska", "anna@example.com", 25)


def test_free_spots_at_start():
    fc = FitnessClass("Joga", make_trainer(), 5)
    assert fc.free_spots() == 5


def test_add_member_reduces_spots():
    fc = FitnessClass("Joga", make_trainer(), 5)
    fc.add_member(make_member(1))
    assert fc.free_spots() == 4


def test_is_full():
    fc = FitnessClass("Joga", make_trainer(), 1)
    fc.add_member(make_member(1))
    assert fc.is_full() is True


def test_full_class_raises():
    fc = FitnessClass("Joga", make_trainer(), 1)
    fc.add_member(make_member(1))
    with pytest.raises(ValueError):
        fc.add_member(make_member(2))


def test_duplicate_member_raises():
    fc = FitnessClass("Joga", make_trainer(), 5)
    member = make_member(1)
    fc.add_member(member)
    with pytest.raises(ValueError):
        fc.add_member(member)


def test_invalid_capacity_raises():
    with pytest.raises(ValueError):
        FitnessClass("Joga", make_trainer(), 0)
