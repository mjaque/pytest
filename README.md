## Introdução aos testes em Python com o pytest

**Objetivos:**

- Reconhecer a importancia dos testes no desenvolvimento de aplicações informáticas.
- Aprender os conceitos básicos da criação e execução de testes utilizando o pytest para melhorar a fiabilidade do código.

**Definição:** Os testes garantem que o código se comporta conforme o esperado. O pytest é uma poderosa estrutura de testes que simplifica a criação de testes e oferece funcionalidades avançadas, como __fixtures__ e __parametrização__. É utilizado para testes unitários, testes de integração e pipelines de integração contínua, com o objetivo de detetar erros numa fase inicial do desenvolvimento.

**Referência da documentação:**

- https://docs.pytest.org/en/stable/getting-started.html
- https://realpython.com/pytest-python-testing/
- https://docs.python.org/3/library/unittest.html

**Debate:** Qual é o papel dos testes no desenvolvimento de software? Vantagens e desvantagens. [Conheces o Alex Hannold?](https://www.youtube.com/watch?v=leCAy1v1fnI "National Geographic")

**Tutorial:**

- Criar uma função simples (e.g., somar).
```py
# app.py
def somar(a, b):
    return a + b
```
- Escrever o teste para a função.
```py
# test_app.py
from app import somar

def test_somar():
    assert somar(2, 3) == 6
    # Sim, primeiro fazemos com que o teste falhe.

if __name__ == "__main__":
    test_somar()
	
```
- Execute o teste utilizando:
```bash
    python3 test_app.py
```

**Os testes sao mais fáceis com pytest**

- Instalar o pytest:
```bash
    pip install pytest
```

- Executar os testes:
```bash
    pytest
```

_pytest_ procura ficheiros com nomes `_test.py` e vai executar as funções com os nomes `test_?`. Além disso apresenta os resultados a cors. 


## Exercício:

Programar um teste para um classificador de sardinhas:
```py
class Classificador:

    MEDIDAS =  (7, 9, 11, 13, 14)
    DESTINOS = ("free","tapas", "canning", "frozen", "grill", "portions")

    
    def classificar(self, sardinha):
        for medida, destino in zip( self.MEDIDAS, self.DESTINOS):
            if sardinha < medida:
                return destino
        return self.DESTINOS[-1]

if __name__ == "__main__":
    classificador = Classificador()
    print(classificador.classificar(3))
    print(classificador.classificar(8.3))
    print(classificador.classificar(10))
    print(classificador.classificar(12))
    print(classificador.classificar(13.4))
    print(classificador.classificar(15))
```

Vai ter de utilizar a parametrização do pytest.


## Challenge:

Temos aquí uma applicaçao muito simples com o patrao de Modelo-Vista-Controlador. Façam testes unitários para todas as classes, mas se quiserem que sejam verdadeiramente unitários, cada teste deve ser independente das outras classes. E, para isso, vão precisar de criar objetos "mock".

app.py
```py
from controlador import Controlador


if __name__ == "__main__":
    Controlador()

```

controlador.py
```py 
from vista import Vista
from modelo import Modelo


class Controlador:
    def __init__(self):
        # Cria a vista e o modelo
        self.vista = Vista()
        self.modelo = Modelo()

        # Pede os dados à vista
        pessoa = self.vista.perguntar()

        # Envia a pessoa para o modelo
        self.modelo.guardar(pessoa)

        print("Processo concluído com sucesso.")

```

vista.py
```py
from pessoa import Pessoa


class Vista:
    def perguntar(self):
        # Pede ao utilizador os dados da pessoa
        nome = input("Introduza o nome: ")
        idade = int(input("Introduza a idade: "))

        # Cria e devolve o objeto Pessoa
        pessoa = Pessoa(nome, idade)
        return pessoa

```

pessoa.py
```py
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"

```

modelo.py
```py 
class Modelo:
    def __init__(self):
        # Lista onde as pessoas serão guardadas
        self.pessoas = []

    def guardar(self, pessoa):
        # Guarda o objeto pessoa na lista
        self.pessoas.append(pessoa)

```

