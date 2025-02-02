class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    Rafael = Mutante(nome='Rafael')
    Paulo = Homem(Rafael, nome='Paulo')
    print(Pessoa.cumprimentar(Paulo))
    print(id(Paulo))
    print(Paulo.cumprimentar())
    print(Paulo.nome)
    print(Paulo.idade)
    for filho in Paulo.filhos:
    print(filho.nome)
    Paulo.sobrenome = 'Cruz'
    del Paulo.filhos
    Paulo.olhos = 1
    del Paulo.olhos
    print(Paulo.__dict__)
    print(Rafael.__dict__)
    print(Pessoa.olhos)
    print(Paulo.olhos)
    print(Rafael.olhos)
    print(id(Pessoa.olhos), print(Paulo.olhos), print(Rafael.olhos))
    print(Pessoa.metodo_estatico(), Paulo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Paulo.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Paulo, Pessoa))
    print(isinstance(Paulo, Homem))
    print(Paulo.olhos)
