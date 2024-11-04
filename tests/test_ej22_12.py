import pytest
from src.bucles.ej22_12 import comprobar_letra, letra_en_frase

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
    
    
def test_frase():
    assert letra_en_frase("dalmata", "a") == 3
    assert letra_en_frase("doce", "x") == 0
    assert letra_en_frase("mamamamamama", "m") == 6

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("jcreyes", "s", 1),
        ("juanito69", "o", 1),
        ("ratatouille", "l", 2),
        ("murcielago", "r", 1),
        ("posponer", "q", 0)
    ]
)
def test_frase_params(input_n1, input_n2, expected):
    assert letra_en_frase(input_n1, input_n2) == expected