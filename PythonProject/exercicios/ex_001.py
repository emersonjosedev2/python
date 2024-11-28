
quantidade_notas = int(input("Quantas notas serão calculadas?"))

contador_notas = int(0)

lista = []

contar = int(len(lista))

while (contar <= quantidade_notas - 1):

    if quantidade_notas != int:
        n = int(input("digite sua a nota"))
        print("Apenas números")

        lista.append(n)
        print(contar)
        print(lista)
        contar = int(len(lista))

    else:
        print("Apenas números" )

print(sum(lista))
