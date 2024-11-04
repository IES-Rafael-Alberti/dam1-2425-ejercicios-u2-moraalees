import pytest
from src.condicionales.ej21_03 import comprobar_cero, dividir_numeros

def test_division():
    assert dividir_numeros(8, 4) == 2.00
    assert dividir_numeros(10, 3) == 3.3333333333333335
    assert dividir_numeros(2, 2) == 1.00

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (2, 4, 0.50),
        (1000, 2, 500.00),
        (3, 6, 0.50),
        (1005, 5, 201.00),
        (9, 3, 3.00)
    ]
)
def test_division_params(input_n1, input_n2, expected):
    assert dividir_numeros(input_n1, input_n2) == expected
    
    
def test_cero():
    assert comprobar_cero(0) == False
    assert comprobar_cero(0.9) == True
    assert comprobar_cero(5) == True

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (0, False),
        (8.7, True),
        (0, False),
        (0.0000001, True),
        (0, False)
    ]
)
def test_cero_params(input_n1, expected):
    assert comprobar_cero(input_n1) == expected