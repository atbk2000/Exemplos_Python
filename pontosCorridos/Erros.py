#Arquivo com funções para detecção de erros

import Interface.Constantes as Constantes

#Recebe times pertencentes a uma rodada e avalia a ocorrência
#de erros (mesmo time duas vezes em uma rodada)
#Retorna o índice dos times repetidos
def detectar_erro(rodada):
    times_repetidos = []
    i = 0
    while rodada != []:
        repetiu = False
        if rodada.count(i) >= 2:
            repetiu = True
        while rodada.count(i) > 0:
            rodada.remove(i)
        if repetiu:
            times_repetidos.append(i)
        i += 1
    return times_repetidos


#Detecção de erros na lista confrontos
#Se um mesmo time ocorrer duas vezes ou mais em uma rodada, erro
#Verifica todas as rodadas
def verificaRodadas():
    contador = 0
    qtd_times = Constantes.qtd_times
    confrontos = Constantes.confrontos
    while contador <= len(confrontos) - qtd_times:
        rodada = confrontos[contador:contador + qtd_times]
        times_repetidos = detectar_erro(rodada)
        if times_repetidos != []:
            i = 0
            while i in range(len(times_repetidos)):
                print(f'Erro: o time com índice {times_repetidos[i]} ocorre mais de uma vez na rodada {int((contador/qtd_times)+1)}.')
                i += 1
        else:
            print(f'Rodada {int((contador/qtd_times)+1)} está ok!')
        contador += qtd_times

