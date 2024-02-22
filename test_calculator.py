# test_calculator.py
from calculator import (
    dodavannya,
    vidnimannya,
    mnozhennya,
    dilennya,
    cilochislenne_dilennya,
    osta4a_vid_cilochislenogo_dilennya,
)
import pytest


def test_dodavannya():
    assert dodavannya(1, 2) == 3
    assert dodavannya(-1, 1) == 0
    assert dodavannya(10, -5) == 5


def test_vidnimannya():
    assert vidnimannya(1, 2) == -1
    assert vidnimannya(-1, 1) == -2
    assert vidnimannya(10, -5) == 15


def test_mnozhennya():
    assert mnozhennya(2, 3) == 6
    assert mnozhennya(-2, 3) == -6
    assert mnozhennya(2, -3) == -6


def test_dilennya():
    assert dilennya(6, 3) == 2
    assert dilennya(7, 2) == 3.5
    assert dilennya(10, 0) == "Помилка: ділення на нуль"


def test_cilochislenne_dilennya():
    assert cilochislenne_dilennya(7, 2) == 3
    assert cilochislenne_dilennya(10, 3) == 3
    assert cilochislenne_dilennya(10, 0) == "Помилка: ділення на нуль"


def test_osta4a_vid_cilochislenogo_dilennya():
    assert osta4a_vid_cilochislenogo_dilennya(7, 2) == 1
    assert osta4a_vid_cilochislenogo_dilennya(10, 3) == 1
    assert osta4a_vid_cilochislenogo_dilennya(10, 0) == "Помилка: ділення на нуль"


# Додайте інші тести за необхідності

if __name__ == "__main__":
    pytest.main()
