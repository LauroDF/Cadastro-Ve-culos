from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade_carga):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade_carga = capacidade_carga
    
    def __str__(self):
        retornar = super().__str__()
        return f''' {retornar}
- Capacidade Carga: {self.__capacidade_carga}'''


'''from Veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, n_portas):
        super().__init__(marca, modelo, placa, ano)
        self.__n_portas = n_portas
    # Overrite = Sobreescrever o método __str__()
    def __str__(self):
        ret = super().__str__()
        return f''' #{ret}
#- Num. Portas: {self.__n_portas}'''