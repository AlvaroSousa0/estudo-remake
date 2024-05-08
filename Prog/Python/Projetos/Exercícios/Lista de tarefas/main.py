'''
Faça uma lista de tarefas com as seguintes opções:
    Adicionar tarefa 
    Listar tarefas 
    Opção de desfazer(a cada vez que chamarmos, desfaz a ultima ação.)
    Opção de refazer (a cada vez que chamarmos,refaz a ultima ação.)

'''

tarefas = []
tarefa_undo = []

while True:
    try:

        acao = input('\nDigite uma tarefa ou (undo,redo ou list): ')
        
        if acao == 'undo':

            if len(tarefas) == 0:
                print('Nada a desfazer. ')
            else:
                tarefa_undo.append(tarefas[-1])
                tarefas.pop()
            continue
        elif acao == 'redo':

            if len(tarefa_undo) == 0:
                print('Nada a refazer. ')
            else:
                tarefas.append(tarefa_undo[-1])
                tarefa_undo.pop()
            continue
        elif acao == 'list':
            print(tarefas)
            continue
        else:
             tarefas.append(acao)
    except IndexError:
        pass