"""
Você deverá criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção


O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

1) Valor de direção com valores possíveis: Norte, Sul, Leste e Oeste
2) Método girar_a_direita
3) Método girar_a_esquerda

   N
 O   L
   S


    Exemplo:
    >>> # Testando o motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Testando a direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> # Testando o Carro
    >>> motor = Motor()
    >>> direcao = Direcao()
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    3
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    1
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_a_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_a_direcao()
    'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_a_direcao()
    'Sul'
    >>> carro.girar_a_direita()
    >>> carro.calcular_a_direcao()
    'Oeste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_a_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Norte'

"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(0, self.velocidade - 2)


class Direcao:
    NORTE = 'Norte'
    SUL = 'Sul'
    LESTE = 'Leste'
    OESTE = 'Oeste'

    _rotacao_a_direita_dict = {
        NORTE: LESTE,
        LESTE: SUL,
        SUL: OESTE,
        OESTE: NORTE,
    }

    _rotacao_a_esquerda_dict = {
        NORTE: OESTE,
        OESTE: SUL,
        SUL: LESTE,
        LESTE: NORTE,
    }

    def __init__(self):
        self.valor = self.NORTE

    def girar_a_direita(self):
        self.valor = self._rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self._rotacao_a_esquerda_dict[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_a_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
