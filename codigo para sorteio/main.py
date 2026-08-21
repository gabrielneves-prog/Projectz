import random


convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]

premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

contador = 0 

while contador < 5:
    premio = random.sample(premios, k=1)
    convidado = random.sample(convidados, k=1)
    contador += 1
    print(f'{convidado} recebeu {premio}') 
