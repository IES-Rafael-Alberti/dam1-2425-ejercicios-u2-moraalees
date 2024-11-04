import pytest
from src.ej22_20 import comprobar_letra, buscar_letra

def test_letra():
    assert comprobar_letra("4") == False
    assert comprobar_letra("tiroides") == False
    assert comprobar_letra("P") == True

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("2", False),
        ("h", True),
        ("eee", False),
        ("l", True),
        ("g.", False)
    ]
)
def test_letra_params(input_n1, expected):
    assert comprobar_letra(input_n1) == expected
    
    
def test_letras():
    assert buscar_letra("germany", "r") == 7
    assert buscar_letra("hienas del congo", "x") == 16
    assert buscar_letra("culiacan", "c") == 8

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("w", "w", 1),
        ("julieta69", "u", 9),
        ("trex", "x", 4),
        ("ÑOPG", "f", 4),
        ("4", "e", 1)
    ]
)
def test_letras_params(input_n1, input_n2, expected):
    assert buscar_letra(input_n1, input_n2) == expected