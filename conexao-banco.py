import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=LEVI-95;"
    "Database=Cadastro_sistema_levi;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")
