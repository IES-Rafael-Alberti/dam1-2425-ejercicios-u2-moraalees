import pytest
from src.condicionales.ej21_02 import intro_contraseña

def test_contrasena():
    assert intro_contraseña("contraseña") == False
    assert intro_contraseña("CONtrAsena") == True
    assert intro_contraseña("namibia") == False

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("contRASENA", True),
        ("CONTRASEÑA", False),
        ("maractus", False),
        ("contraseba", False),
        ("contrasena", True)
    ]
)
def test_contrasena_params(input_n1, expected):
    assert intro_contraseña(input_n1) == expected