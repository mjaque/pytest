from exercicio_2.modelo import Modelo
from exercicio_2.pessoa import Pessoa


def test_guardar_pessoa_no_modelo():
    modelo = Modelo()
    pessoa = Pessoa("João", 25)

    modelo.guardar(pessoa)

    assert len(modelo.pessoas) == 1
    assert modelo.pessoas[0].nome == "João"
    assert modelo.pessoas[0].idade == 25
