# test_somar_pytest.py
import pytest
import random

from app import somar

@pytest.fixture
def dados_validos():
    return [2, 3, 5]

def test_somar_bem(dados_validos):
    assert somar(dados_validos[0], dados_validos[1]) == dados_validos[2]

@pytest.fixture
def dados_nomeados():
    return {"param_1": 2, "param_2": 3, "resultado": 5}

def test_somar_outro(dados_nomeados):
    assert somar(dados_nomeados["param_1"], dados_nomeados["param_2"]) == dados_nomeados["resultado"]


@pytest.fixture
def dados_random():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    r = a + b
    return (a, b, r)

def test_somar_random(dados_random):
    assert somar(dados_random[0], dados_random[1]) == dados_random[2]


@pytest.fixture
def fixture_complexa():
    # Create data
    # Connect to test data base
    # Do some stuff

    return {"param_1": 2, "param_2": 3, "resultado": 5}

