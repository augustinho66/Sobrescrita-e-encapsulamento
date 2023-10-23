class cachorro():
    def __init__(self, tamanho, peso, psi):
        self._tamanho = tamanho
        self._peso = peso
        self._psi = psi
@property
def peso(self):
 return self._peso
@property
def tamanho(self):
 return self._tamanho
@property
def psi(self):
 return self._psi
@psi._setter
def psi (self, psi):
    self._psi = psi
@peso._setter
def peso (self, psi):
    self._peso = peso
@tamanho._setter
def psi (self, psi):
    self._tamanho = tamanho

peso = input()
psi = input()
tamanho = input()
objeto=cachorro(peso, psi, tamanho,)