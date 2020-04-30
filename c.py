''# '''
# três aspas simples ou duplas são utilizadas para fazer comentários grandes
# '''
#
# # a hastag é utilizada p fazer comentário de uma linha
#
# # comando para escrever
# print('Texto a ser mostrado')
#
# # comando escrita formatada
# nome = 'Cassia'
# verdades = 'linda e cheirosa'
# print(f'{nome} {verdades}')
#
# print('{} {}'.format('Cassia', 'Vadiaaaaaa'))
#
# # comando para centralizar texto
# print(f"{'Cassia':^30}")  # centraliza no meio de 30 espaços
# print(f"{'Cassia':>30}")  # centraliza no final de 30 espaços
# print(f"{'Cassia':<30}")  # centraliza no inicio de 30 espaços
#
# # comando para exibir quantidades de casas decimais escolhida
# print(f"{2 / 3:.2f}")
#
# # comando para importar
# import math  # carrega todos os funções da biblioteca
# from math import pow, sqrt  # carrega funções especificas
#
# # comando p ajuda
# help('math')  # comando p o python console
# print(help('math'))  # comando p o arquivo
#
# '''
#     Operadores matematicos
#
#     ==  - pergunta se é igual
#     !=  - diferente
#     <   - menor
#     >   - maior
#     <=  - menor ou igual
#     >=  - maior ou igual
# '''
#
# """
#     Operadores logicos
#
#     and
#     or
#     !
#     xor
# """
#
# '''
#     Operadores condicionais
#
#     if condição:
#         algum comando
#
#     elif outra condição:
#         algum comando
#
#     else:
#         algum comando
# '''
#
# """
# pedir entrada do usuario
#
# 1 == um
# 2 == dois
# 3 == tres
#
# e de acordo com entrada printar seu correspondente
#
# caso não seja nenhuma das opçõs printar "Opção não cadastrada"
#
# """
#
# valor = int(input('Escolha um numero entre 1 2 e 3:'))
#
# if (valor == 1):
#     print('um')
#
# elif (valor == 2):
#     print('dois')
#
# elif (valor == 3):
#     print("tres")
#
# else:
#     print('Opção não cadastrada')
#
# for i in ['cassia', 2, 3, 'klesley']:
#     print(i, end=', ')
#
# for i in range(9, 0, -2):
#     print(i)
#
# for i in range(4):
#     valor = int(input('Escolha um numero entre 1 2 e 3:'))
#
#     if (valor == 1):
#         print('um')
#
#     elif (valor == 2):
#         print('dois')
#
#     elif (valor == 3):
#         print("tres")
#
#     else:
#         print('Opção não cadastrada')
#

# idade = input('digite a idade CERTA: ').strip()
#
# while not idade.isnumeric():
#     idade = input('voce nao digitou um numero valido, digite novamente (Para sair, digite -1): ').strip()
#
#     if idade.isnumeric():
#         print('agr sim vacilao')
#         break
#
#     elif idade == '-1':
#         print('q pena q desistiu')
#         break
#
'''
Estruturas básicas
lista
[] ou list()

como declarar:
x = [1,2]
x = list()

adicionar elemento:
x.append(elemento)

remover elemento:
x.pop() #remove ultimo elemento
x.pop(0) #remove elemento na posição 0

ou

del x[0] #apaga elemento na posição 0

#matrizes

nome = [[],[]] #matriz 2x1 #declarar matriz vazia
x.append([1,2,3,4])



TUPLAS

() ou nome = () #declarar

nao remove elemento e não altera


DICIONARIO

{} ou nome = {} #declarar

nome = {'chave':'valor'} #adicionar elemento
'''


'''
FUNÇÕES

def nome(parametro1, parametro2) #declarar funcao 
    comandos
    
def nome(*parametro1) #mando quantos elementos quiser
    comandos
    
def nome(**paramentro) #cria dicionario
    '''

