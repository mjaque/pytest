from exercicio_2.modelo import Modelo


def test_guardar_objeto_no_modelo():
    modelo = Modelo()
    objeto_falso = object() # isto é um 'mock'

    modelo.guardar(objeto_falso)

    assert len(modelo.pessoas) == 1
    assert modelo.pessoas[0] is objeto_falso
