import streamlit as st
from crud import criar_aluno, listar_alunos, atualizar_idade, deletar_aluno

st.set_page_config(page_title="gerenciamento de alunos", page_icon="👨‍🏫")
st.title("Gerenciamento de alunos")
menu = st.sidebar.radio("Menu", ["Inserir", "Listar", "Atualizar", "Deletar"])

if menu == "Inserir":   
    st.subheader("Inserir novo aluno")
    nome = st.text_input("Nome do aluno", placeholder="Seu nome")
    idade = st.number_input("Idade do aluno", min_value=16, max_value=120, step=1)
    if st.button("Criar aluno"):
        if nome.strip() == "":
            st.error("O nome do aluno não pode ser vazio.")
        elif idade == "":
            st.error("A idade do aluno não pode ser vazia.")
        else:
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} com {idade} anos criado com sucesso!")