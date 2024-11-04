import pytest
from src.bucles.ej22_02 import comprobar_edad, contar_anios

def test_edad():
    assert comprobar_edad("5") == True
    assert comprobar_edad("4.4") == False
    assert comprobar_edad("si") == False

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("2", True),
        ("diego ponme un 10 por favor", False),
        ("6666666666", True),
        ("-2.2", False),
        ("100", True)
    ]
)
def test_edad_params(input_n1, expected):
    assert comprobar_edad(input_n1) == expected
    
    
def test_anios():
    assert contar_anios(6) == 6
    assert contar_anios(666) == 666
    assert contar_anios(9) == 9

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (4, 4),
        (1010, 1010),
        (9090, 9090),
        (44, 44),
        (2, 2)
    ]
)
def test_anios_params(input_n1, expected):
    assert contar_anios(input_n1) == expected