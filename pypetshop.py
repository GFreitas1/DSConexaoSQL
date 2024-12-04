#pip install pyodbc


import pyodbc

try:
#Server da escola: localhost
    conexao = pyodbc.connect("DRIVER={SQL server}; SERVER='+FREITAS+';DATABASE='+petshop+';UID='+sa+';PWD='+*123456HAS*")

    queryBanco = conexao.cursor()
    print("funfou legal")
    verificacao = True
except:
    print("tomou no cu")
    verificacao = False

def adicionarpet():

    nomepet = input("Nome do seu pet: ")
    idadepet = input("Idade do seu pet: ")

    criarpet = f"INSERT INTO pet(nome, idade) values ({nomepet}, {idadepet})"
    queryBanco.execute(criarpet)
    queryBanco.commit()

def editarpet():

    idpet = int(input("Digite o id do pet que voce quer alterar: "))
    
    print("""Valores alteraveis: 
          1- Nome
          2- Idade
          3- Nome e idade
          """)

    escolhaedita = int(input("Valor selecionado: "))

    match escolhaedita:
        case 1:
            escolhanome = input("Novo nome: ")

            nomealterado = f"UPDATE pet SET nome = {escolhanome} where id = {idpet}"
            queryBanco.execute(nomealterado)
            queryBanco.commit()
        case 2:
            escolhaidade = input("Nova idade: ")

            idadealterado = f"UPDATE pet SET idade = {escolhaidade} where id = {idpet}"
            queryBanco.execute(idadealterado)
            queryBanco.commit()
        case 3:
            escolhanome = input("Novo nome: ")
            escolhaidade = input("Nova idade: ")

            valoresalterados = f"UPDATE pet SET nome = {escolhanome}, idade = {escolhaedita} where id = {idpet}"
            queryBanco.execute(valoresalterados)
            queryBanco.commit()
        case _:
            print("O seu nigga so tem 3 numeros")

def exibirtabela():
    tabelaescolhida = input("Qual tabela voce quer exibir: ")
    exibetabela = f"SELECT * FROM {tabelaescolhida}"

    queryBanco.execute(exibetabela)

    exibicao = queryBanco.fetchall()

    for row in exibicao:
        print(row)

def deletarpet():
    idpet = int(input("Digite o id do pet que voce quer excluir: "))

    exclusaopet = f"DELETE FROM pet where id = {idpet}"
    queryBanco.execute(exclusaopet)
    queryBanco.commit()

while verificacao:
    
    print("""
    0- Sair
    1- Adicionar pet
    2- Editar pet
    3- Exibir tabela
    4- Deletar pet
    """)

    escolhamenu = int(input("Escolha uma opcao do menu: "))

    match escolhamenu:
        case 0:
            break
        case 1:
            adicionarpet()
        case 2:
            editarpet()
        case 3:
            exibirtabela()
        case 4:
            deletarpet()
