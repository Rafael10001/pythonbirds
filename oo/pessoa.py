class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Rafael = Pessoa(nome='Rafael')
    Paulo = Pessoa(Rafael, nome='Paulo')
    print(Pessoa.cumprimentar(Paulo))
    print(id(Paulo))
    print(Paulo.cumprimentar())
    print(Paulo.nome)
    print(Paulo.idade)
    for filho in Paulo.filhos:
        print(filho.nome)
