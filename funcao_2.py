'''lista_num=[]
def somar (a=0,b=0,c=0):
    s = a+b+c
    lista_num.append(s)
    print(f"A soma deram, {lista_num}")

somar(3,4,7)
somar(3,4,)
somar(3)
'''
'''def somar (a=0,b=0,c=0):
    s = a+b+c
    return s

r1 = somar(3,4,7)
r2 = somar(3,4,)
r3 = somar(3)

print(f"AS somas deram, {r1}, {r2}, {r3}")'''

'''def fatorial (num=1):
    f=1
    for c in range(num,0,-1):
        f*=c
    return f

fat = int(input("DIgite para saber o Fatorial ->"))

print(f"Fatorial de {fat} é {fatorial(fat)}")'''

def parimpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um Nuúmero -> "))

if parimpar(num):
    print("É PAR!")
else:
    print("É IMPAR!")