from src.interfaces import Observador

class Pessoa(Observador):

    def __init__(self):
        self.acordada = False

    def esta_acordada(self):
        return self.acordada

    def update(self):
        print('Bom dia! Acordei.')
        self.acordada = True