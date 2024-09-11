import time, os

class Veiculo:
    # __init__ é o Método Construtor
    def __init__(self, marca, modelo, placa, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
    # Metodo Getters and Setters para os atributos privados
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        if marca != 'Peugeot':
            self._marca = marca.upper()
    
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self._modelo = modelo
    
    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        self.__placa = placa

    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        if ano >= 1900:
            self.__ano = ano

    # Método da instância
    def calcularTempoUso(self):
        return 2024 - self.__ano
    
    def __str__(self):
        return f'''
- Marca: {self.__marca}
- Modelo: {self.__modelo}
- Placa: {self.__placa}
- Ano: {self.__ano}'''

# Abaixo estou instanciando um 
# Objeto da Classe Veiculo
meuUno = Veiculo('Fiat', 'Uno com escada', 'MEN-2017', 2000)
# Alterando o Ano do meuUno
#print (meuUno.get_marca)
#print (meuUno.calcularTempoUso())
meuUno.__ano = 2010
#print (meuUno.calcularTempoUso())

teuFusca = Veiculo('Volks', 'Fusca do Itamar', 'BAT-2004', 1995)

#Criando uma instância da classe veiculo
uno = Veiculo("Fiat", "Uno", "ABC", 2005)
#print(uno)
#print(uno.__str__())

'''
print (meuUno.calcularTempoUso())
print (teuFusca.calcularTempoUso())

time.sleep (4)
os.system ('cls')

print("")'''
