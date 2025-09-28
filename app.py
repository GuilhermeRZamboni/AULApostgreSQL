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
            st.error("O nome do aluno não pode ser vazio")
        else:
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} com {idade} anos criado com sucesso!")
elif menu == "Listar":
    st.subheader("Listar alunos")
    alunos = listar_alunos() 

    if alunos:
        tabela_alunos = [{"ID": linha[0], "Nome": linha[1], "Idade": linha[2]} for linha in alunos]
        st.table(tabela_alunos)
    else:
        st.write("Nenhum aluno encontrado")

elif menu == "Atualizar":
    st.subheader("Atualizar idade do aluno")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Selecione o ID do aluno:", [linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova idade do aluno", min_value=16, max_value=120, step=1)
        if st.button("Atualizar idade"):
            atualizar_idade(id_aluno, nova_idade)
            st.success(f"Idade do aluno com ID {id_aluno} atualizada para {nova_idade} anos!")
    else:
        st.info("Nenhum aluno encontrado para atualizar")