import json
import os

# Cadastrar Aluno
def cadastrar_aluno():
    global alunos
    nome = input ("Nome de aluno: ")
    notas = []
    for i in range (1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)

    aluno = {"nome": nome, "notas": notas}
    alunos.append(aluno)
    salvar_alunos()
    print (f"Aluno '{nome}' cadastrado com sucesso.")

# Listar alunos
def listar_alunos():
    if not alunos:
        print ("Nenhum aluno cadastrado.")
        return
    
    print ("\n--- Lista de alunos ---")
    for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]
        media = sum(notas) / len(notas)
        print(f"{nome} - Notas: {notas} - Média: {media:.2f}")

# Remover aluno
def remover_aluno():
    global alunos
    nome = input("Digite o nome do aluno a remover: ")

    for aluno in alunos:
        if aluno ["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            salvar_alunos()
            print(f"Aluno '{nome}' removido com sucesso.")
            return
    
    print (f"Aluno '{nome}' não encontrado.")

# Editar notas
def editar_notas():
    global alunos
    nome = input("Digite o nome do aluno que deseja editar a nota: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print (f"Notas atuais de {aluno['nome']}: {aluno['notas']}")
            novas_notas = []
            for i in range (1, 4):
                nota = float(input(f"Digite a nova {i}ª nota: "))
                novas_notas.append(nota)
            aluno["notas"] = novas_notas
            salvar_alunos()
            print (f"Nota de '{nome}' atualizadas com sucesso.")
            return
    
    print (f"Aluno '{nome} não encontrado.'")

# Média Geral da turma
def media_geral ():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    soma_das_medias = 0

    for aluno in alunos:
        media = sum(aluno["notas"]) / len(aluno["notas"])
        soma_das_medias += media
    
    media_geral = soma_das_medias/len(alunos)
    print (f"Media geral da turma: {media_geral:.2f}")

# Carrega dados se existir
def carregar_alunos():
    if os.path.exists("alunos.json"):
        with open ("alunos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []
    
# Salvar os dados no arquivo
def salvar_alunos():
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump (alunos, arquivo, indent=4, ensure_ascii=False)

# Exibe o menu principal
def mostrar_menu():
    print("\n=== SISTEMA DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Editar notas")
    print("5 - Média geral da turma")
    print("6 - Sair")

# Inicializa a lista
alunos = carregar_alunos()
print(f"Alunos carregados: {len(alunos)} encontrado(s).")

# Laço principal
while True:
    mostrar_menu()
    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        remover_aluno()
    elif opcao == "4":
        editar_notas()
    elif opcao == "5":
        media_geral()
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")