class Restaurante:

    def __init__(self, nome, categoria, ativo,idade, cidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.idade = idade
        self.cidade = cidade

        ativo = False

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

        

restaurante_formatado = Restaurante(nome = "Teste", categoria="Teste")
print(restaurante_formatado)
