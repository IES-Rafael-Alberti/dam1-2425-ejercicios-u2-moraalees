import pytest
from src.ej21_04 import comprobar_entero, comprobar_numero

def test_entero():
    assert comprobar_entero("5") == True
    assert comprobar_entero("5.00001") == False
    assert comprobar_entero("fuerza valencia") == False

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("2", True),
        ("ratatouille", False),
        ("6666666666.1", False),
        ("-25.11", False),
        ("3", True)
    ]
)
def test_entero_params(input_n1, expected):
    assert comprobar_entero(input_n1) == expected
    
    
    
    
def test_numero():
    assert comprobar_numero(5) == False
    assert comprobar_numero(88) == True
    assert comprobar_numero(69) == False

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (2, True),
        (21, False),
        (99999, False),
        (90000000001, False),
        (4, True)
    ]
)
def test_numero_params(input_n1, expected):
    assert comprobar_numero(input_n1) == expected