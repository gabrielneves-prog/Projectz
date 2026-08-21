import string
import random

senha = string.ascii_letters + string.digits + string.punctuation

while True:
    parada = input("Digite S para sair ou qualquer tecla para continuar: ").lower()

    if parada == 's':
        print("Programa finalizado.")
        break

    gerador = ''.join(random.sample(senha, k=8))
    print(f"Sua senha é: {gerador}")