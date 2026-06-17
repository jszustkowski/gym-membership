"""Testy klasy Payment."""

import pytest

from gym import Member, Payment


def make_member():
    return Member(1, "Anna", "Kowalska", "anna@example.com", 25)


def test_payment_not_paid_by_default():
    payment = Payment(make_member(), 100.0)
    assert payment.paid is False


def test_pay_sets_paid():
    payment = Payment(make_member(), 100.0)
    payment.pay()
    assert payment.paid is True


def test_negative_amount_raises():
    with pytest.raises(ValueError):
        Payment(make_member(), -50.0)

def test_refund_after_paid():
    payment = Payment(make_member(), 100.0)
    payment.pay()
    payment.refund()
    assert payment.paid is False


def test_refund_without_paying_raises():
    payment = Payment(make_member(), 100.0)
    with pytest.raises(ValueError):
        payment.refund()