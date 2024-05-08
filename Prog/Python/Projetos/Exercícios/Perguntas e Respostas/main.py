perguntas = {
    'Pergunta 1': {
    'Pergunta': 'Quanto é 2 + 2? ',
    'Respostas': {'a':'5','b':'4','c':'8','d':'14'},
    'resposta certa':'b'},

    'Pergunta 2': {
    'Pergunta': 'Quanto é 3 * 5? ',
    'Respostas': {'a':'1','b':'30','c':'5','d':'15'},
    'resposta certa':'d'},
    
    'Pergunta 3': {
    'Pergunta': 'Quanto é 2⁴? ',
    'Respostas': {'a':'16','b':'4','c':'2','d':'18'},
    'resposta certa':'a'},
    
    'Pergunta 4': {
    'Pergunta': 'Quanto é 1000 - 7? ',
    'Respostas': {'a':'990','b':'1007','c':'993','d':'300'},
    'resposta certa':'c'},

    'Pergunta 5': {
    'Pergunta': 'Quanto é 1 + 1? ',
    'Respostas': {'a':'10','b':'2','c':'45','d':'11'},
    'resposta certa':'b'},

    'Pergunta 6': {
    'Pergunta': 'Quanto é 4³ * 10 - 35? ',
    'Respostas': {'a':'605','b':'10','c':'5','d':'3425'},
    'resposta certa':'a'}
}
acertos = 0

for pk, pv in perguntas.items():
    print(pv['Pergunta'])

    for rk, rv in pv['Respostas'].items():
        print(f'[{rk}]  {rv} ')

    resposta = input('Qual é a resposta certa? ')

    if resposta.lower() == pv['resposta certa']:
        print()
        print ('Resposta Correta! ')
        print()
        acertos += 1
    else:
        print()
        print('Resposta errada!')
        print()

print(f'Taxa de acerto: {(int(acertos) * 100) / len(perguntas)}%')
print(f'Você deu {acertos} respostas corretas para {len(perguntas)} perguntas. ')
