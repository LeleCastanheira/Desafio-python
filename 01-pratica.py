cont = 0
informacoes = []
print('\033[1;34m***Cadastro de alunos da Ultima School***\n')

while (cont < 1):
    nome = input('Digite o seu nome: ')
    informacoes.append(nome)
    cont+=1

print("\033[1;35m\n\n**Você conseguiu finalizar o desafio**\n")

for nome in informacoes:
    print(f'Parabêns {informacoes}')
