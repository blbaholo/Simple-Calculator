from simple_calculator.calculator import add, multiply


def test_add_two_integers() -> None:
    assert add(1, 2) == 3


def test_add_multiple_integers() -> None:
    assert add(1, 2, 3) == 6


def test_add_negative_integers() -> None:
    assert add(-1, -1) == -2


def test_multiply_two_integers() -> None:
    assert multiply(1, 3) == 3


def test_multiply_negative_and_postive_integers() -> None:
    assert multiply(-1, 3) == -3


def test_multiply_multiple_integers() -> None:
    assert multiply(1, 2, 3, 4, 5) == 120
