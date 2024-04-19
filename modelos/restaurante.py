from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []

    def __init__(self, nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | Avaliacao')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}  ')

    # Metodo para os objetos
    def alternar_estado(self): 
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else 'Falso'
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)   

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self,item):
        #isInstance compara se o item é uma instancia do objeto ou de objeto que herda essa classe
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        
    @property    
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        # Estou iterando a lista cardapio salvando no item o objeto em si e no i o index
        for i,item in enumerate(self._cardapio,start=1):
            # Estou olhando se no item tem esse atributo descricao
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preco: R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preco: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)                








