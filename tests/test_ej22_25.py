import pytest
from src.ej22_25 import contador

def test_palabras():
    assert contador("hyundai es porquería") == "porquería"
    assert contador("la gallina turuleta") == "turuleta"
    assert contador("si a veces") == "veces"

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("ayunta al 15 por fin", "ayunta"),
        ("ford tourneo super", "tourneo"),
        ("cuarenta", "cuarenta"),
        ("nicaragua, maragua", "nicaragua,"),
        ("sudeste asiatico", "asiatico")
    ]
)
def test_palabras_params(input_n1, expected):
    assert contador(input_n1) == expected