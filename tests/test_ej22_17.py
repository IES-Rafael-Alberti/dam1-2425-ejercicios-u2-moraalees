import pytest
from src.bucles.ej22_17 import comprobar_entero, dividir_sumar_numero

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
    
    
    
    
    
def test_sumatorio():
    assert dividir_sumar_numero("81") == 9
    assert dividir_sumar_numero("303") == 6
    assert dividir_sumar_numero("29266") == 25

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("2", 2),
        ("723", 12),
        ("888", 24),
        ("610", 7),
        ("77", 14)
    ]
)
def test_sumatorio_params(input_n1, expected):
    assert dividir_sumar_numero(input_n1) == expected