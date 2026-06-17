"""Testy klasy Membership."""

import pytest

from gym import Member, Membership


def make_member():
    return Member(1, "Anna", "Kowalska", "anna@example.com", 25)


def test_membership_active_by_default():
    membership = Membership(make_member(), "Standard", 120.0, 30)
    assert membership.is_active() is True


def test_deactivate():
    membership = Membership(make_member(), "Standard", 120.0, 30)
    membership.deactivate()
    assert membership.is_active() is False


def test_negative_price_raises():
    with pytest.raises(ValueError):
        Membership(make_member(), "Standard", -10.0, 30)


def test_membership_stores_data():
    membership = Membership(make_member(), "Premium", 200.0, 90)
    assert membership.plan_name == "Premium"
    assert membership.days == 90

def test_describe_active():
    membership = Membership(make_member(), "Standard", 120.0, 30)
    assert "aktywny" in membership.describe()


def test_describe_inactive():
    membership = Membership(make_member(), "Standard", 120.0, 30)
    membership.deactivate()
    assert "nieaktywny" in membership.describe()
