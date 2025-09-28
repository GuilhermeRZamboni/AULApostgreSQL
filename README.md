# Gerenciamento de Alunos

Este projeto é uma aplicação web simples para gerenciar alunos utilizando Python, Streamlit e PostgreSQL. Permite inserir, listar, atualizar e deletar registros de alunos em um banco de dados PostgreSQL.

## Funcionalidades

- **Inserir aluno:** Adicione novos alunos informando nome e idade.
- **Listar alunos:** Visualize todos os alunos cadastrados.
- **Atualizar idade:** Altere a idade de um aluno existente.
- **Deletar aluno:** Remova alunos do banco de dados.

## Tecnologias Utilizadas

- Python
- Streamlit
- PostgreSQL
- psycopg2
- python-dotenv

## Estrutura do Projeto

- [`app.py`](app.py): Interface principal com Streamlit.
- [`crud.py`](crud.py): Funções de manipulação do banco de dados (CRUD).
- [`db.py`](db.py): Conexão com o banco de dados PostgreSQL.
- `.env`: Variáveis de ambiente para configuração do banco de dados.
- `requirements.txt`: Dependências do projeto.

## Como Executar

1. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

2. Configure o arquivo `.env` com os dados do seu banco PostgreSQL.

3. Certifique-se de que a tabela `alunos` existe no banco de dados:
    ```sql
    CREATE TABLE alunos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100),
        idade INTEGER
    );
    ```

4. Execute o aplicativo:
    ```sh
    streamlit run app.py
    ```

## Observações

- O projeto utiliza variáveis de ambiente para segurança dos dados de acesso ao banco.
- Para modificar a estrutura do banco, altere o SQL conforme necessário.

## Licença

Este projeto é