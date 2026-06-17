"""Testy klasy Member."""

import pytest

from gym import Member


def test_full_name():
    member = Member(1, "Anna", "Kowalska", "anna@example.com", 25)
    assert member.full_name() == "Anna Kowalska"


def test_is_adult_true():
    member = Member(1, "Anna", "Kowalska", "anna@example.com", 25)
    assert member.is_adult() is True


def test_is_adult_false():
    member = Member(2, "Jan", "Nowak", "jan@example.com", 16)
    assert member.is_adult() is False


def test_invalid_email_raises():
    with pytest.raises(ValueError):
        Member(3, "Ewa", "Lis", "zly-email", 30)
