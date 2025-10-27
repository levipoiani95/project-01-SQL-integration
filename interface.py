import streamlit as st
import pandas as pd
import numpy as np
import funcoes
from datetime import date   


st.title("Sistema de cadastro de paciente:")

#todos_exames = ["Clinico", "Eletro-cardio", "Eletro-Encefalo", "Coleta de sangue" ]

nome = st.text_input("Digite seu nome completo")
idade = st.text_input("Digite sua idade")

min_allowed_date = date(1900,1,1)
max_allowed_date = date(2025, 12, 31)
data_nascimento = st.date_input("Digite sua data de nascimento",format="DD/MM/YYYY",
                                min_value=min_allowed_date,
                                max_value=max_allowed_date,
                                value=date(1990,1,1)
)
empresa = st.text_input("Digite o nome da sua empresa")
cargo = st.text_input("Digite seu cargo na empresa")

exames = st.text_input("Selecione o(s) exame(s) solicitados para hoje:")
#separador = " "
#exames = separador.join(exames)

if st.button("Adicionar cadastro"):
    funcoes.inserir_dados(nome,idade,data_nascimento,empresa,cargo,exames)
    st.success("Cadastro Concluído")

if st.button("Mostrar pacientes"):
    dados = funcoes.listar_dados()
    dados = np.array(dados)
    columns = ['nome','idade','data_nascimento','empresa','cargo','exames']
    df = pd.DataFrame(data=dados,columns=columns)  
    st.header("Lista de Pacientes")
    st.table(df)
    
