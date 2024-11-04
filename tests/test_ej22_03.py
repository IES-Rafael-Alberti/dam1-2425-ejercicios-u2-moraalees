import pytest
from src.bucles.ej22_03 import comprobar_entero, contador_numeros

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
    
    
def test_contador():
    assert contador_numeros(43) == 43
    assert contador_numeros(1) == 1
    assert contador_numeros(314159) == 314159

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (26, 26),
        (53589, 53589),
        (79, 79),
        (3, 3),
        (433, 433)
    ]
)
def test_contador_params(input_n1, expected):
    assert contador_numeros(input_n1) == expected