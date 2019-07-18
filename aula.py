# login = "wagner"
# senha = "teste"

# if login == "wagner" and senha == "teste"
#     print("entrado")
#     else:print("saido")

# import random
# print("Digite seu nome:")
# nome = input()

# print("O nome digitado foi "+nome)

# 1
# print("Digite seu salario")
# salario = int(input())
# print("Digite o valor solicitado")
# emprestimo = int(input())
# print("Digite sua idade")
# idade = int(input())
# salario*=10
# if emprestimo>salario or idade<25:
#     print("Nao podemos te ajudar")
# else:print("O valor foi aprovado")

# 2

# print("Coloque o numero de degraus")
# degraus = int(input())

# print("Coloque o material da escada")
# material=input()
# temp=material

# i=0
# while i<degraus:
#     print(temp)
#     temp=material+temp
#     i+=1

# 3
# import random
# nomes=['rafael', 'ana', 'leo', 'gabriel']
# print(random.shuffle(nomes))



# 4     


# nomes_feminino=["ana","vitoria", "paula"]
# nomes_masculino=["rafael""gabriel", "joao"]

# total_feminino=len(nomes_feminino)
# total_masculino=len(nomes_masculino)
# par=1
# par_total=0

# while total_feminino>0:
#     if total_masculino>0:
#         par=par*total_masculino
#         total_feminino=total_feminino-1
#         par_total=par+par_total
#         par=1


# print(par_total)

# 4.1

# import random
# nomes_feminino=["ana","vitoria", "paula"]
# nomes_masculino=["rafael","gabriel", "joao"]

# sorteio=random.choice(nomes_feminino)
# sorteio=sorteio+" e "+random.choice(nomes_masculino)

# print(sorteio)


# 5
# import random
# nomes_feminino=["ana","vitoria", "paula"]
# nomes_masculino=["rafael","gabriel", "joao"]
# nomes=nomes_feminino+nomes_masculino

# i = 1
# j = 0

# for pessoa1 in nomes:
#     for k in range(j, len(nomes)):
#         if pessoa1 != nomes[k]:
#             print("parzinho " +pessoa1+ " e " +nomes[k])
#             i+=1
# j+=1

# 6


# iguais = ['a', 'a', 'a', 'a', 'a']
# diferentes = ['b', 'b', 'b', 'b', 'b',]

# def todos_iguais(lista):
#     for i in range(i, len(lista)):
#         if lista[i] != lista[i - 1]:
#             return lista

# print(iguais)

# def separar_nome(nome_completo):
#     lista = nome_completo.split()
#     return lista[0], lista[1]
    
# separar_nome("wagner rafael")

def somar(*args):
    total = 0
    for valor in args:
        total+= valor
    print(total)
somar(1, 2)

# def media(nome, *notas):
#     total = 0
#     for nota in notas:
#         total += nota
#     print(total)

