# Gym Membership — System zarządzania członkostwem w siłowni

Prosty system do obsługi siłowni: członkowie, karnety, trenerzy, zajęcia
grupowe i płatności. Projekt napisany w czystym Pythonie.

## Wymagania projektu

- model dziedzinowy złożony z co najmniej 5 klas,
- typowanie argumentów i wartości zwracanych,
- podział kodu na kilka plików,
- dokumentacja każdej klasy i funkcji (docstring),
- co najmniej 15 testów jednostkowych i 3 testy integracyjne,
- praca zespołowa na GitHubie (gałęzie, pull requesty, code review).

## Funkcjonalności

- rejestracja członków i sprawdzanie pełnoletności,
- karnety (cena, czas trwania, aktywacja/dezaktywacja),
- trenerzy ze specjalizacją,
- zajęcia grupowe z limitem miejsc i kontrolą zapisów,
- płatności i sumowanie przychodu,
- klasa `Gym` spinająca całość.

## Klasy

| Klasa | Plik | Opis |
|-------|------|------|
| `Member` | `src/gym/member.py` | Członek siłowni |
| `Membership` | `src/gym/membership.py` | Karnet członka |
| `Trainer` | `src/gym/trainer.py` | Trener |
| `FitnessClass` | `src/gym/fitness_class.py` | Zajęcia grupowe |
| `Payment` | `src/gym/payment.py` | Płatność |
| `Gym` | `src/gym/gym.py` | Główna klasa siłowni |

## Struktura projektu

```
gym-membership/
├── README.md
├── requirements.txt
├── pytest.ini
├── demo.py
├── src/gym/
│   ├── __init__.py
│   ├── member.py
│   ├── membership.py
│   ├── trainer.py
│   ├── fitness_class.py
│   ├── payment.py
│   └── gym.py
└── tests/
    ├── conftest.py
    ├── test_member.py
    ├── test_membership.py
    ├── test_trainer.py
    ├── test_fitness_class.py
    ├── test_payment.py
    ├── test_gym.py
    └── test_integration.py
```

## Instalacja i uruchomienie

Wymagany Python 3.10 lub nowszy.

```bash
git clone https://github.com/jszustkowski/gym-membership.git
cd gym-membership
pip install -r requirements.txt

python demo.py   # przykład użycia
pytest           # uruchomienie testów
```

## Przykład użycia

```python
from gym import Gym, Member, Membership, Payment, Trainer, FitnessClass

gym = Gym("FitZone")

anna = Member(1, "Anna", "Kowalska", "anna@example.com", 25)
gym.add_member(anna)

karnet = Membership(anna, "Standard", 120.0, 30)
gym.register_payment(Payment(anna, karnet.price))

trener = Trainer(1, "Marek Zieliński", "joga")
joga = FitnessClass("Joga poranna", trener, 10)
gym.add_class(joga)
joga.add_member(anna)

print(gym.member_count())   # 1
print(gym.total_income())   # 120.0
print(joga.free_spots())    # 9
```

## Zespół i obowiązki

| Osoba | Gałąź | Zakres |
|-------|-------|--------|
| Jakub Szustkowski | `feature_member` | `Member` + testy |
| _(uzupełnić)_ | `feature_membership` | `Membership` + testy |
| _(uzupełnić)_ | `feature_trainer` | `Trainer` + testy |
| _(uzupełnić)_ | `feature_class` | `FitnessClass` + testy |
| _(uzupełnić)_ | `feature_payment` | `Payment`, `Gym` + testy |

## Praca z GitHubem

- Gałęzie stałe: `main` (wersje gotowe) i `dev` (integracja).
- Każda funkcjonalność na osobnej gałęzi `feature_*` odbitej od `dev`.
- Zmiany trafiają do `dev` przez Pull Request z przynajmniej jednym review.
- Po zakończeniu pracy `dev` scalany do `main` z tagiem wersji (np. `v1.0`).
