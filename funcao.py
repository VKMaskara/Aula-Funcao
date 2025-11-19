def contador(num):
    tam = len(num)
    soma = sum(num)
    print(f"Recebi {tam} são eles respectivamente {num} e a soma deles é {soma}")

minha_linta = []

while True:
    minha_linta.append(int(input("Digite um numero -> ")))
      
    condi = input("Deseja adicionar mais um? (s/n)")

    if condi == 'n':
        contador(minha_linta)
        print("Programa encerrado.")
        break'

lista_dobra = []
def dobra(lst):
    pos = 0
    while pos < len(lst):  # Changed from <= to < to avoid index error
        lst[pos] *= 2
        pos += 1
    print(f"Lista dobrada: {lst}")

while True:
    lista_dobra.append(int(input("Digite um numero -> ")))
      
    condi = input("Deseja adicionar mais um? (s/n)")

    if condi == 'n':

        dobra(lista_dobra)

        print("Programa encerrado.")
        break

def teste():
    n = 2
    print(f"Na função teste, n vale {n}")

n =3
print(f"No programa principal, n vale {n}")
teste()