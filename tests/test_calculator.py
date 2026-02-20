from src.calculator import add


def test_add():
    assert add(2, 3) == 5, (
        "AUTO_FIX_TARGET: Edit src/calculator.py -> function add(a, b) must return a + b"
    )
