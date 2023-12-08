# Teste Elevador
import random

from elevador import Elevador

# Criação e instância de um objeto da classe elevador
e1 = Elevador(0, True, random.random() * 1000)

# Exibindo o elevador parado
print('\n\t\t\t -- Elevador Parado --\n')
print(e1)

# Subindo...
print('\n\t\t\t -- Subir -- ')
e1.subir(5)

# Exibindo o elevador no 5º andar
print('\n\t\t\t -- Elevador no 5º andar --\n')
print(e1)


