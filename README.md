# Gym Membership — System zarządzania członkostwem w siłowni

## Wymagania projektu

- model dziedzinowy złożony z co najmniej 5 klas,
- typowanie argumentów i wartości zwracanych,
- podział kodu na kilka plików,
- dokumentacja każdej klasy i funkcji (docstring),
- co najmniej 15 testów jednostkowych i 3 testy integracyjne,
- praca zespołowa na GitHubie (gałęzie, pull requesty, code review).

## Funkcjonalności

- rejestracja członków i sprawdzanie pełnoletności,
- karnety (cena, czas trwania, aktywacja/dezaktywacja, opis),
- trenerzy ze specjalizacją i sprawdzaniem kompetencji,
- zajęcia grupowe z limitem miejsc, zapisywaniem i wypisywaniem członków,
- płatności wraz ze zwrotami (refund) i sumowaniem przychodu,
- klasa `Gym` spinająca całość (członkowie, zajęcia, płatności, raporty).

## Klasy

| Klasa | Plik | Opis |
|-------|------|------|
| `Member` | `src/gym/member.py` | Członek siłowni (dane, wiek, pełnoletność) |
| `Membership` | `src/gym/membership.py` | Karnet członka (cena, czas trwania, status) |
| `Trainer` | `src/gym/trainer.py` | Trener i jego specjalizacja |
| `FitnessClass` | `src/gym/fitness_class.py` | Zajęcia grupowe z limitem miejsc |
| `Payment` | `src/gym/payment.py` | Płatność (opłacenie, zwrot) |
| `Gym` | `src/gym/gym.py` | Główna klasa zarządzająca siłownią |

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
Sam kod źródłowy korzysta wyłącznie z biblioteki standardowej Pythona.
Pakiet `pytest` jest potrzebny jedynie do uruchamiania testów.

## Testy

Projekt zawiera **35 testów**: 32 jednostkowe oraz 3 integracyjne,
symulujące pełne przepływy (rejestracja → karnet → zajęcia → przychód).

| Plik | Liczba testów |
|------|---------------|
| `test_member.py` | 4 |
| `test_membership.py` | 6 |
| `test_trainer.py` | 4 |
| `test_fitness_class.py` | 8 |
| `test_payment.py` | 5 |
| `test_gym.py` | 5 |
| `test_integration.py` | 3 (integracyjne) |

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
| Jakub Szustkowski | `feature_member` | Klasa `Member`, struktura projektu, README + testy |
| Karol Poznański | `feature_payment` | Klasy `Payment` i `Gym` (`refund`, `average_payment`) + testy |
| Michał Stachowski | `feature_class` | Klasa `FitnessClass` (`remove_member`) + testy |
| Vadym Boichuk | `feature_membership` | Klasy `Membership` i `Trainer` (`describe`, `is_specialist_in`) + testy |

## Praca z GitHubem

- Gałęzie stałe: `main` (wersje gotowe) i `dev` (integracja).
- Każda funkcjonalność powstawała na osobnej gałęzi `feature_*` odbitej od `dev`.
- Zmiany trafiały do `dev` przez Pull Request z recenzją (code review) innej osoby.
- Po scaleniu wszystkich funkcjonalności `dev` został zmergowany do `main`
  i oznaczony tagiem wersji `v1.0`.
