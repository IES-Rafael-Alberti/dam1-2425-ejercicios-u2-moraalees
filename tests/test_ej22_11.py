import pytest
from src.bucles.ej22_11 import ensenar_letras

def test_palabra():
    assert ensenar_letras("5") == "5"
    assert ensenar_letras("guapo") == "guapo"
    assert ensenar_letras("el 10 pls") == "el 10 pls"

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("2", "2"),
        ("francia malos", "francia malos"),
        ("false", "false"),
        ("programacion es facil", "programacion es facil"),
        ("mentira lol", "mentira lol")
    ]
)
def test_palabra_params(input_n1, expected):
    assert ensenar_letras(input_n1) == expected