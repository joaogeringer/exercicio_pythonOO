#poo no python exercicio 1

class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self,nome=nome

    def set_ender(self, ender):
        self.ender=ender

    def get_nome(self):
        return self.nome 

    def get_ender(self):
        return self.ender

#objeto pessoa

pessoa1 = Pessoa('Maria', 'Rua 1')
pessoa2 = Pessoa('João', 'Rua 2')

#imprimir cada um dos objetos
#pesso1
print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')

#pessoa2
print(f'Nome: {pessoa2.get_nome()}, Endereço:{pessoa2.get_ender()}')
        
