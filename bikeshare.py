# coding: utf-8
# !/usr/bin/python3

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento no formato CSV...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Dados lidos com sucesso!")

# Vamos verificar quantas linhas nós temos
print('Número de linhas: {}'.format(len(data_list)))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0:")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")

# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados. OK
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for row in data_list[:20]:
    print(row)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Cabeçalho = campos
# 0 => 'Start Time'
# 1 => 'End Time'
# 2 => 'Trip Duration'
# 3 => 'Start Station'
# 4 => 'End Station'
# 5 => 'User Type'
# 6 => 'Gender'
# 7 => 'Birth Year'

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")

# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas OK
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for row in data_list[:20]:
    gender = row[6]  # posição 6
    print('Na linha {} Gênero é {}'.format(data_list.index(row), gender))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")


# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem OK
def column_to_list(data, index):
    """
    Função que converte os valores das colunas em uma nova lista
    Argumentos:
        param1: lista com os dados organizados em linhas e colunas
        param2: índice da coluna de interesse
    Retorna:
        lista dos dados da coluna de interesse
    """
    column_list = []
    for row in data:
        column_list.append(row[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])
# print(column_to_list(data_list, 6)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[
    1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem


# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso. OK
genders = column_to_list(data_list, -2)
male = 0
female = 0
other_values = 0
for gender in genders:
    if gender == "Male":
        male += 1
    elif gender == "Female":
        female += 1
    else:
        other_values += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista. OK
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função que conta o gênero dos usuários
    Argumentos:
        param1: lista com os usuários
    Retorna:
        lista com a contagem por gênero de usuário (Masculino e Feminino)
    """
    genders = column_to_list(data_list, -2)
    male = 0
    female = 0
    for gender in genders:
        if gender == "Male":
            male += 1
        elif gender == "Female":
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
    1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Função que conta os gêneros dos usuários
    Argumentos:
        param1: lista com os usuários
    Retorna:
        lista com os valores por gênero dos usuários
    """
    genders = count_gender(data_list)
    answer = ""
    if genders[0] > genders[1]:
        answer = "Male"
    elif genders[0] < genders[1]:
        answer = "Female"
    elif genders[0] == genders[1]:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Masculino", "Feminino"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta. OK

print("\nTAREFA 7: Verifique o gráfico!")


def count_user_type(users):
    """
    Função que conta os tipos de usuário
    Argumentos:
        param1: lista com os usuários
    Retorna:
        lista com os valores por tipo de usuário
    """
    subscriber = 0
    customer = 0
    dependent = 0
    for user in users:
        if user == "Subscriber":
            subscriber += 1
        elif user == "Customer":
            customer += 1
        elif user == "Dependent":
            dependent += 1
    return [subscriber, customer, dependent]


users_types = column_to_list(data_list, -3)

print("\nImprimindo resultado de count_user_type:")
print(count_user_type(users_types))

types = ["Assinantes", "Clientes", "Dependente"]
quantity = count_user_type(users_types)
# print('Quantidade=', quantity)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A afirmação é falsa pois existem registros da lista onde o gênero é nulo. Portanto o total de linhas não é igual a quantidade de gêneros cadastrados."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana. OK
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = sorted(list(map(int, trip_duration_list)))  # ordena a lista de duração da viagem

min_trip = 0.
max_trip = 0.
sum_trip = 0.
mean_trip = 0.
median_trip = 0.

min_trip = trip_duration_list[0]  # o primeiro elemento é o mínino
max_trip = trip_duration_list[-1]  # o último elemento é o máximo


def calculate_mean_trip(list_duration):
    """
    Função que calcula a média de duração das viagens
    Argumentos:
        param1: lista com as durações das viagens
    Retorna:
        o valor média
    """
    sum_duration = 0
    for duration in list_duration:
        sum_duration += int(duration)
    mean_trip = round(sum_duration / len(list_duration))
    return mean_trip


def calculate_median_trip(list_duration):
    """
    Função que calcula a mediana de duração das viagens
    Argumentos:
        param1: lista com as durações das viagens
    Retorna:
        o valor da mediana (elemento que separa a metade da amostra)
    """
    size = len(list_duration)
    if size % 2 == 0:
        # caso o tamanho da lista seja par
        m1 = size // 2
        # localiza o termo central
        m2 = m1 + 1
        # localiza o termo próximo e cálcula a média
        return (list_duration[m1] + list_duration[m2]) / 2
    else:
        # caso o tamanho da lista seja ímpar
        index = round((size + 1) / 2)
        return list_duration[index]


mean_trip = calculate_mean_trip(trip_duration_list)
median_trip = calculate_median_trip(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set() OK
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#       """
#       Função de exemplo com anotações.
#       Argumentos:
#           param1: O primeiro parâmetro.
#           param2: O segundo parâmetro.
#       Retorna:
#           Uma lista de valores x.
#
#       """

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

"""Função para agrupar valores iguais e contar o número de ocorrências.
Argumentos:
data: lista com os valores.
Retorna:
Uma lista com [<valores>] e [<ocorrencias>].
"""


def count_items(column_list):
    """
    Função para agrupar os valores iguais e contar o número de ocorrências
    Argumentos:
        param1: lista com os valores
    Retorna:
        lista com os valores iguais e o número de ocorrências
    """
    item_types = []
    count_items = []
    for content in column_list:
        # se não existir, adiciona o item
        if content not in item_types:
            item_types.append(content)
            count_items.append(1)
        else:
            # se existir, incrementa o contador
            index = item_types.index(content)
            count_items[index] += 1
    return [item_types, count_items]


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
else:
    print("Fim...")
