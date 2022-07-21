import Interface.Constantes as Constantes
import Operacoes
import Clube
import Memoria

rodada = 1
times = []
#Guarda índices dos times da lista 'Confrontos'
indices = []


#Inicializa os times com seus parâmetros: jogos, vitórias, empates...
#Tudo é inicializado em 0
def inicializarTimes():
    global times
    emOrdem = Constantes.times_em_ordem

    for i in range(len(emOrdem)):
        clube = Clube.Clube(emOrdem[i], 0, 0, 0, 0, 0, 0, 0, i)
        times.append(clube)


#Adiciona índice de um time à lista 'lista'
def pushIndice(indice):
    global indices

    if indice not in indices:
        indices.append(indice)


#Limpa a lista 'indices'
def clearIndices():
    global indices
    indices.clear()


#Retorna uma lista dos gols dos mandantes e dos visitantes dos confrontos alterados
def golsModificados():
    global indices
    mandantes, visitantes = [], []

    for i in range(len(indices)):

        #Time mandante
        if indices[i] % 2 == 0:
            mandantes.append(indices[i])

            if not ((indices[i] + 1) in indices):
                visitantes.append(indices[i] + 1)

        #Time visitante
        else:
            visitantes.append(indices[i])

            if not ((indices[i] - 1) in indices):
                mandantes.append(indices[i] - 1)

    return mandantes, visitantes


#Desfaz resultado de uma partida para adição de novo resultado
#Deve atualizar a tabela de classificação
def desfazerResultado(indice):
    if indice % 2 == 0:
        mandante = indice
        visitante = indice + 1
        pushIndice(visitante)
    else:
        mandante = indice - 1
        pushIndice(mandante)
        visitante = indice

    if Memoria.getGol(mandante) != '  ' and Memoria.getGol(visitante) != '  ':
        analisarConfronto(mandante, -1)
        atualizarClassificacao(mandante)
        analisarConfronto(visitante, -1)
        atualizarClassificacao(visitante)


#Atualiza a classificação com os novos resultados
def atualizar():
    global indices

    if indices == []:
        return

    mandantes, visitantes = golsModificados()

    for i in range(len(mandantes)):
        if Memoria.getGol(mandantes[i]) != '  ' and Memoria.getGol(visitantes[i]) != '  ':
            analisarConfronto(mandantes[i])
            atualizarClassificacao(mandantes[i])
            analisarConfronto(visitantes[i])
            atualizarClassificacao(visitantes[i])


#Analisa gols do time em uma partida e altera os seus atributos
#Recebe índice do time na lista 'Confrontos'
#Desfaz um resultado se manter = -1
def analisarConfronto(time, manter = 1):
    
    if time % 2 == 0:
        gol = Operacoes.stringToInt(Memoria.getGol(time))
        golAdversario = Operacoes.stringToInt(Memoria.getGol(time + 1))
    else:
        golAdversario = Operacoes.stringToInt(Memoria.getGol(time - 1))
        gol = Operacoes.stringToInt(Memoria.getGol(time))

    pos = getPosicao(Constantes.confrontos[time])

    global times

    #Quantidade de jogos
    times[pos].jogos += 1 * manter

    #Gols pró
    times[pos].gp += gol * manter

    #Gols contra
    times[pos].gc += golAdversario * manter

    #Vitória 
    if gol > golAdversario:
        times[pos].vitorias += 1 * manter
        times[pos].pontuacao += 3 * manter

        if manter == 1:
            times[pos].resultados = 'V'
        elif manter == -1:
            times[pos].resultados = 'D'

    #Empate
    elif gol == golAdversario:
        times[pos].empates += 1 * manter
        times[pos].pontuacao += 1 * manter

        if manter == 1:
            times[pos].resultados = 'E'
        elif manter == -1:
            times[pos].resultados = 'D'

    #Derrota
    elif gol < golAdversario:
        times[pos].derrotas += 1 * manter

        if manter == 1:
            times[pos].resultados = 'D'
        elif manter == -1:
            times[pos].resultados = 'V'


#Alterna posições dos times A e B
#'timeA' é a posição do time A e 'timeB' é a posição do time B
def trocarPosicao(timeA, timeB):
    global times

    aux = times[timeA]
    times[timeA] = times[timeB]
    times[timeB] = aux


#Recebe a posição em ordem alfabética de um time
#Retorna a posição do time
def getPosicao(alfPos):
    global times
    pos = 0

    while times[pos].posAlf != alfPos:
        pos += 1

    return pos


#Faz o time subir de posição até ficar abaixo de um time com melhores atributos
#Ou faz o time subir até a primeira colocação
def subirPosicao(pos):
    #if pos == 0:
    #    return

    global times

    times[pos].resultados = ''

    while pos != 0:
        if times[pos - 1].pontuacao > times[pos].pontuacao:
            break

        elif times[pos - 1].pontuacao == times[pos].pontuacao:
            if times[pos - 1].vitorias > times[pos].vitorias:
                break

            elif times[pos - 1].vitorias == times[pos].vitorias:
                if times[pos - 1].saldoGols() > times[pos].saldoGols():
                    break

                elif times[pos - 1].saldoGols() == times[pos].saldoGols():
                    if times[pos - 1].gp > times[pos].gp:
                        break

        trocarPosicao(pos, pos - 1)
        pos -= 1


#Faz o time descer de posição até ficar acima de um time com piores atributos
#Ou faz o time descer até a última colocação
def descerPosicao(pos):
    global times

    #if pos == len(times) - 1:
    #    return

    times[pos].resultados = ''

    while pos != len(times) - 1:
        if times[pos + 1].pontuacao < times[pos].pontuacao:
            break

        elif times[pos + 1].pontuacao == times[pos].pontuacao:
            if times[pos + 1].vitorias < times[pos].vitorias:
                break

            elif times[pos + 1].vitorias == times[pos].vitorias:
                if times[pos + 1].saldoGols() < times[pos].saldoGols():
                    break

                elif times[pos + 1].saldoGols() == times[pos].saldoGols():
                    if times[pos + 1].gp < times[pos].gp:
                        break

        trocarPosicao(pos, pos + 1)
        pos += 1


#Atualiza a tabela de classificação
#Prioridade: pontuação > vitórias > saldo de gols > gols pró
def atualizarClassificacao(time):
    global times

    pos = getPosicao(Constantes.confrontos[time])

    if times[pos].resultados == 'V' or times[pos].resultados == 'E':
        subirPosicao(pos)
    elif times[pos].resultados == 'D':
        descerPosicao(pos)


    
    
        