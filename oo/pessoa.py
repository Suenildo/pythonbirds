class Pessoa:
    def cumprimentar(self):
        return f' olá {id(self)}'  # o retorno da função é olá


if __name__ == '__main__':
    p = Pessoa()          # atribuindo o objeto p a classe Pessoa
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())  # não é necessário passar o  parâmetro.
