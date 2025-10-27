import pyodbc


dados_conexao = (
    "Driver={SQL Server};"
    "Server=LEVI-95;"
    "Database=Cadastro_sistema_levi;"
)

def conecta_banco():
    conexao = pyodbc.connect(dados_conexao)
    return conexao

def inserir_dados(nome,idade,data_nascimento,empresa,cargo,exames):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = f"""INSERT INTO Cadastro(nome, idade, data_nascimento, empresa, cargo, exames) 
                VALUES('{nome}', {idade}, '{data_nascimento}', '{empresa}', '{cargo}', '{exames}')"""
    cursor.execute (comando)
                        
    conexao.commit() #SALVAR OPERACOES DO BANCO 
    conexao.close() #FECHA A CONEXAO

def listar_dados():
    conexao = conecta_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cadastro")
    dados = cursor.fetchall() #transforma os dados em lista, sem ele viria endreço da memoria
    cursor.close()
    return dados
   