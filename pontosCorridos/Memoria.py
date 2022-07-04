import Operacoes

posInicial = 0
qtdClubes = 0
#Armazena os gols em formato de string
resultados = []

#A rodada sempre começa em 1 nos parâmetros das funções

#Analisa o arquivo Resultados.txt e decide se é necessário
#formatá-lo com uma nova quantidade de times.
#Retorna 1 se arquivo foi formatado
#Retorna -1 se arquivo não foi formatado
def iniciar(qtdTimes):

    global posInicial, qtdClubes, resultados

    posinicial = Operacoes.grandeza(qtdTimes) + 1
    qtdClubes = qtdTimes

    #Armazena gols feitos por um determinado time em uma determinada rodada
    resultados = ['  '] * (qtdTimes - 1) * qtdTimes * 2

    with open('Resultados.txt', 'r') as file:
        qtdLida = Operacoes.stringToInt(lerPosicao(0))

        if qtdLida != qtdTimes:
            #O arquivo é renovado
            formatarArquivo()
            return 1
        else:
            #Dados armazenados da última simulação são relembrados
            lerArquivo()
            return -1


#Lê os gols dos times no arquivo 'Resultados.txt' e os 
#armazena na lista 'resultados'
def lerArquivo():

    global posInicial, qtdClubes, resultados
    pos = posInicial

    with open('Resultados.txt', 'r') as file:

        rodadas = file.readlines()

        for rodada in range(1, len(rodadas)):
            for gol in range(qtdClubes):
                golLido = getGolArquivo(rodadas, rodada, gol*3)
                setGol((rodada - 1) * qtdClubes + gol, golLido)
       

#Formata o arquivo 'Resultados.txt' de acordo com a 
#a lista 'resultados'. Os resultados armazenados no arquivo
#são baseados na lista 'resultados'
def formatarArquivo():

    global qtdClubes, resultados

    with open('Resultados.txt', 'w') as file:

        file.write(str(qtdClubes) + '\n')

        for i in range(len(resultados)):

            if len(resultados[i]) == 1:
                file.write(resultados[i] + ' ')
            else:
                file.write(resultados[i])

            if (i + 1) % qtdClubes == 0:
                file.write('\n')
            else:
                file.write('.')


#Lê determinada posição do arquivo 'Resultados.txt'
#Sempre lê 2 posições
def lerPosicao(pos):

    with open('Resultados.txt', 'r') as file:
        file.seek(pos)
        
        return file.read(2)


#Insere a quantidade de gols que determinado time fez em 
#uma rodada. Armazena-se na lista 'Resultados' no índice 'indice'. 
def setGol(indice, gols):
    global resultados

    resultados[indice] = str(gols)


#Retorna gol(s) em determinada posição da lista 'resultados'
def getGol(indice):
    global resultados

    return resultados[indice]


#Lê a lista bidimensional 'rodadas'
#'rodadas' é gerada a partir do arquivo 'Resultados.txt'
def getGolArquivo(rodadas, rodada, gol):

    caracter1 = rodadas[rodada][gol]
    caracter2 = rodadas[rodada][gol + 1]

    return caracter1 + caracter2


#Salva a classificação no arquivo 'Classificacao.txt'
def salvarClassificacao(times):
    with open('Classificacao.txt', 'w') as file:

        for time in times:

            file.write(str(time.posAlf) + ' ')

            file.write(str(time.pontuacao) + ' ')

            file.write(str(time.jogos) + ' ')

            file.write(str(time.vitorias) + ' ')

            file.write(str(time.empates) + ' ')

            file.write(str(time.derrotas) + ' ')

            file.write(str(time.gp) + ' ')

            file.write(str(time.gc) + '\n')

    return


#Retorna a lista de times em ordem de classificação de acordo
#com a última execução do programa
def timesSalvos():

    import Clube
    from Interface.Constantes import times_em_ordem

    times = []

    with open('Classificacao.txt', 'r') as file:

        linhas = file.readlines()

    for linha in linhas: 

        char = ''
        pos = 0

        while linha[pos] != ' ':
            char += linha[pos]
            pos += 1

        #Posição alfabética do clube
        posAlf = Operacoes.stringToInt(char)

        #Nome do clube
        nome = times_em_ordem[posAlf]

        pos += 1
        char = ''

        while linha[pos] != ' ':
            char += linha[pos]
            pos += 1

        #Pontuação do clube
        pontuacao = Operacoes.stringToInt(char)

        pos += 1
        char = ''

        while linha[pos] != ' ':
            char += linha[pos]
            pos += 1

        #Quantidade de jogos do clube
        jogos = Operacoes.stringToInt(char)

        pos += 1
        char = ''

        while linha[pos] != ' ':
            char += linha[pos]
            pos += 1

        #Vitórias do clube
        vitorias = Operacoes.stringToInt(char)

        pos += 1
        char = ''

        while linha[pos] != ' ':
            char += linha[pos]
            pos += 1

        #Empates do clube
        empates = Operacoes.stringToInt(char)

        pos += 1
        char = ''

        while linha[pos] != ' ':
            char += linha[pos]
            pos += 1

        #Derrotas do clube
        derrotas = Operacoes.stringToInt(char)

        pos += 1
        char = ''

        while linha[pos] != ' ':
            char += linha[pos]
            pos += 1

        #Gols pró do clube
        gp = Operacoes.stringToInt(char)

        pos += 1
        char = ''

        while linha[pos] != '\n':
            char += linha[pos]
            pos += 1

        #Gols contra do clube
        gc = Operacoes.stringToInt(char)

        clube = Clube.Clube(nome, pontuacao, jogos, vitorias, empates,
                            derrotas, gp, gc, posAlf)

        times.append(clube)

    return times

