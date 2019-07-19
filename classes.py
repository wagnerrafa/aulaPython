import random
NAIPES = ['Paus', 'Copas', 'Espada', 'Ouros']
RANKS = ['As', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove','Dez', 'Dama', 'Valete', 'Reis']

class Carta():
  def __init__(self, naipe, rank, valor):
    self.naipe = naipe
    self.rank = rank
    self.valor = valor

  def __str__(self):
    return f'{self.rank} de {self.naipe} [{self.valor}]'

class Baralho():
  def __init__(self):
    self.cartas = []
    i=1
    for naipe in NAIPES:
        for rank in RANKS:
            carta = Carta(naipe, rank, i)
            self.adicionar_carta(carta)
            i+=1
            if i>10:
                i=1

  def __str__(self):
    if len(self.cartas) == 0:
      return '[VAZIO]' 

    string = ''
    
    for carta in self.cartas:
      string += str(carta)
      string += ', '

    return string

  def adicionar_carta(self, carta):
    self.cartas.append(carta)

  def remover_carta(self):
    return self.cartas.pop()
