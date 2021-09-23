class Veiculo:
    velocidade = 100
    #fator_de_frenagem = -8  # m/s**2
    #fator_de_aceleracao
    def __init__(self, tipo, chassi, marca, modelo, ano,fator_de_frenagem,fator_de_aceleracao):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def freio(self, velocidade_final):
        print(
            f"reduzindo a velocidade de {self.velocidade} para {velocidade_final}")
        dv = (velocidade_final - self.velocidade)*3.6
        return f'levara um total de {dv/self.fator_de_frenagem}s'

    def acelerar(self, velocidade_desejada):
        """v=v0+A*T"""

        return f'acelerando {self.velocidade}'


class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada


class Carro(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, qt_portas):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.qt_portas = qt_portas


corola = Carro(tipo='corrida_turbinado', chassi=122121,
               marca='toyota', modelo='corola', ano=2021, qt_portas=4)


print(corola.freio(40))
