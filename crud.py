from db import conectar

def criar_aluno(nome, idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("INSERT INTO alunos(nome, idade) VALUES (%s, %s)", 
                        (nome, idade))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar aluno: {erro}")
        else:
            print("Aluno criado com sucesso!")
        finally:
            cursor.close()
            conexao.close()
def listar_alunos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM alunos ORDER BY id")
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao tentar listar alunos: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_idade(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("UPDATE alunos SET idade = %s WHERE id = %s",
                           (nova_idade, id_aluno))
            conexao.commit()
            
        except Exception as erro:
            print(f"Erro ao tentar atualizar idade: {erro}")
        else:
            print("Idade do aluno alterada com sucesso!")
        finally:
            cursor.close()
            conexao.close()
# lista = listar_alunos()

# for aluno in lista:
#     print(f"Idade - {aluno[0]} - Nome: {aluno[1]} - Idade: {aluno[2]}")
# id = int(input("Digite o id do aluno que você deseja alterar a idade: "))
# idade = int(input("Digite a nova idade do aluno: "))
# atualizar_idade(id, idade)


def deletar_aluno(id):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM alunos WHERE id = %s",
                (id,))
            conexao.commit()
            
        except Exception as erro:
            print(f"Erro ao tentar atualizar idade: {erro}")
        else:
            print("Aluno deletado com sucesso!")
        finally:
            cursor.close()
            conexao.close()
