"""Testy klasy Trainer."""

from gym import Trainer


def test_trainer_attributes():
    trainer = Trainer(1, "Marek Nowak", "joga")
    assert trainer.name == "Marek Nowak"
    assert trainer.specialty == "joga"


def test_describe():
    trainer = Trainer(1, "Marek Nowak", "joga")
    assert trainer.describe() == "Marek Nowak (joga)"
