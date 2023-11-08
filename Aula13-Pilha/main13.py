from Livro import Livro
from Pilha import Pilha

l1 = Livro("O Tempo e o Vento", "Érico Veríssimo")
l2 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien")
l3 = Livro("E não restou nenhum", "Agatha Christie")
l4 = Livro("Dom Casmurro", "Machado de Assis")

pilha = Pilha()

pilha.imprimir()

pilha.add(l1)
pilha.add(l2)
pilha.add(l3)
pilha.remover()
pilha.add(l4)
pilha.remover()
pilha.remover()
pilha.remover()
