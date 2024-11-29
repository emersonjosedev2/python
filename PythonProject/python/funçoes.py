
def erro(erro):
    return print(erro)

def Lnota(lnotas):
    return int(len(lnotas))

q_notas = int(input("Quantas notas?"))
lista = []
ler = Lnota(lista)

while ler < q_notas :
    n1 = input("Digite a nota")
    lista.append(n1)
    ler = Lnota(lista)
    print(ler)





def nome (nome):

    return f"Hola {nome} "


print(nome("Emerson jose "))


