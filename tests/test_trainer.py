"""Testy klasy Trainer."""

from gym import Trainer


def test_trainer_attributes():
    trainer = Trainer(1, "Marek Nowak", "joga")
    assert trainer.name == "Marek Nowak"
    assert trainer.specialty == "joga"


def test_describe():
    trainer = Trainer(1, "Marek Nowak", "joga")
    assert trainer.describe() == "Marek Nowak (joga)"

def test_is_specialist_in_true():
    trainer = Trainer(1, "Marek", "Joga")
    assert trainer.is_specialist_in("joga") is True


def test_is_specialist_in_false():
    trainer = Trainer(1, "Marek", "joga")
    assert trainer.is_specialist_in("crossfit") is False
