from src import *

a1 = Alarme()
p1 = Pessoa()
p2 = Pessoa()
p3 = Pessoa()
a1.addPessoa(p1)
a1.addPessoa(p2)
a1.addPessoa(p3)
a1.tocar()
print(p1.esta_acordada())