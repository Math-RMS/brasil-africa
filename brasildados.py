from conexao import conectar
def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()
    # Criando um objetivo cursor para executr as consultas SQL
    cursor = conn.curssor()
    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tb_brasil")
    # Obter resultados
    resultados = cursor.fetchall()
    # Imprimir resultados
    for resultado in resultados:
        print(resultado)
    # Fechar a conexao e o cursor 
    cursor.close()
    conn.close()
    
def inserir(ID_tribo, nome_tribo, num_habit, renda_mensal, escolariedade, trab_assa):
    # Abrir uma conexão com o banco de dados
    conn = conectar()
    # Criando um objetivo cursor para executr as consultas SQL
    cursor = conn.curssor()
    # Executar a consulta SQL para interigir um novo registro 
    sql = "INSERT INTO tb_brasil (ID_tribo, nome_tribo, num_habit, renda_mensal, escolariedade, trab_assa) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (ID_tribo, nome_tribo, num_habit, renda_mensal, escolariedade, trab_assa)
    cursor.execute(sql, val)
    # Commit da transação 
    conn.commit()
    # Imprimir mensagem de sucesso
    print("Registro inserido com sucesso.")
    #  Fechar a conexão e o cursor 
    cursor.close()
    conn.close()
    
    
def excluir (ID_tribo):
    # Abrir uma conexão com o banco de dados
    conn = conectar()
    # Criando um objetivo cursor para executr as consultas SQL
    cursor = conn.curssor()
    # Executar a consulta SQL para excluir o registro 
    sql = "DELETE FROM tb_brasil WHERE ID_tribo = %s)"
    val = (ID_tribo,)
    cursor.execute(sql, val)
    # Commit da transação 
    conn.commit()
    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")
    # Fechar a conexão e o cursor 
    cursor.close()
    conn.close()
    

conn = conectar()
# Criando um objetivo cursor para executr as consultas SQL
cursor = conn.curssor()
while True:
    #Mostar as opções de operações
    print('O que você deseja?')
    print('1 - listar os estados')
    print('2 - Inserir uma tribo nova')
    print('3 - Deletar uma tribo')
    print('0 - Sair')
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    
    if opcao == 1:
        #Listar estados
        listar(conn, cursor)
    
    elif opcao == 2:
        #Inserir novo estado 
        ID_tribo = int(input("Digite o ID da nova tribo: "))
        nome_tribo = input("Digite o nome da nova tribo: ")
        num_habit = int(input("Digite o número de habitantes da tribo: "))
        renda_mensal = input("Digite a renda mensal da tribo:  ")
        escolariedade = input("Digite o nivel de escolareidade (fundamental, médio ou superior)")
        trab_assa = input("Digite se possuem trabalho assalariado sim ou não: ")
        inserir(ID_tribo, nome_tribo,num_habit, renda_mensal, escolariedade, trab_assa)
        
    elif opcao ==3:
        #Deletar um  estado 
        ID_tribo = int(input("Digite o ID da tribo que seja deletar: "))
        excluir(ID_tribo)
    
    elif opcao == 0:
        #Sair do programa
        break
    
    else:
        print("Opção inválida. Digite novamente. ")
    
    cursor.close()
    conn.close()
