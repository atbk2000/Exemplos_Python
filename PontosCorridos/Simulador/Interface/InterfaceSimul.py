from Interface.classe import interface
import Interface.primitivas as primitivas
import Interface.texto as texto
from Interface.Constantes import * 
import Simulador
import pygame
import Operacoes
import Memoria

#Configura a imagem inicial que aparecerá ao usuário ao iniciar o programa
def inicializarGraficos(screen):
    interface.setSurface(screen)

    desenharFundo()

    desenharClassificacao()
    desenharRodada()

    primitivas.imagem('seta_retorno.png', [SETA_RETORNO[0] + 1, SETA_RETORNO[1] + 1])
    primitivas.imagem('seta_avanco.png', [SETA_AVANCO[0] + 1, SETA_AVANCO[1] + 1])


#Desenha o fundo dos gráficos do simulador
#Função chamada apenas 1 vez
def desenharFundo():
    pygame.display.set_caption('Simulador')
    interface.getSurface().fill(VERDE)

    #Retângulo onde se encontram os atributos dos times
    primitivas.rect(CINZA_CLARO, [RECT_ATRIBUTOS_TIMES[0],
                                            RECT_ATRIBUTOS_TIMES[1],
                                            RECT_ATRIBUTOS_TIMES[2],
                                            ALTURA_RECT])

    #Lacunas para os times na classificação
    for i in range(qtd_times):
        if i % 2 == 0:
            primitivas.rect(CINZA_ESCURO1, [CLASSIFICACAO[0], CLASSIFICACAO[1] + ALTURA_RECT * i,
                                                    CLASSIFICACAO[2], ALTURA_RECT])

        if i % 2 != 0:
            primitivas.rect(CINZA_ESCURO2, [CLASSIFICACAO[0], CLASSIFICACAO[1] + ALTURA_RECT * i,
                                                    CLASSIFICACAO[2], ALTURA_RECT])
  
    #Desenhar os caracteres P, V, E, D, GP, GC e SG
    posicaoY = RECT_ATRIBUTOS_TIMES[1] + 2
    texto.escrever('P', [RECT_ATRIBUTOS_TIMES[0] + 6, posicaoY])
    texto.escrever('J', [RECT_ATRIBUTOS_TIMES[0] + RECT_ATRIBUTOS_TIMES[2] / 8 + 6, posicaoY])
    texto.escrever('V', [RECT_ATRIBUTOS_TIMES[0] + 2 * RECT_ATRIBUTOS_TIMES[2] / 8 + 6, posicaoY])
    texto.escrever('E', [RECT_ATRIBUTOS_TIMES[0] + 3 * RECT_ATRIBUTOS_TIMES[2] / 8 + 6, posicaoY])
    texto.escrever('D', [RECT_ATRIBUTOS_TIMES[0] + 4 * RECT_ATRIBUTOS_TIMES[2] / 8 + 6, posicaoY])
    texto.escrever('GP', [RECT_ATRIBUTOS_TIMES[0] + 5 * RECT_ATRIBUTOS_TIMES[2] / 8 + 2, posicaoY])
    texto.escrever('GC', [RECT_ATRIBUTOS_TIMES[0] + 6 * RECT_ATRIBUTOS_TIMES[2] / 8 + 2, posicaoY])
    texto.escrever('SG', [RECT_ATRIBUTOS_TIMES[0] + 7 * RECT_ATRIBUTOS_TIMES[2] / 8 + 2, posicaoY])

    #Desenhar contorno da tabela de classificação
    primitivas.rect(PRETO, [CLASSIFICACAO[0], CLASSIFICACAO[1], CLASSIFICACAO[2],
                                        ALTURA_RECT * qtd_times], 1)

    #Desenhar os números indicadores de posição
    for i in range(qtd_times):
        texto.escrever(str(i + 1) + '.', [CLASSIFICACAO[0] + 3, 
                                                    ALTURA_RECT * i + CLASSIFICACAO[1] + 2])

    desenharLinhas()

    #Desenhar lacunas para os confrontos
    #Desenhar as caixas de resultados e o x´s dos confrontos
    for i in range(qtd_confrontos + 1):
        if i % 2 == 0:
            primitivas.rect(CINZA_ESCURO1, [POSX_CONFRONTOS, POSY_CONFRONTOS + ALTURA_RECT * i,
                                                    LARGURA_RECT, ALTURA_RECT])

        if i % 2 != 0:
            primitivas.rect(CINZA_CLARO, [POSX_CONFRONTOS, POSY_CONFRONTOS + ALTURA_RECT * i,
                                                    LARGURA_RECT, ALTURA_RECT])


        if i > 0:
            primitivas.rect(PRETO, [CAIXA_MANDANTE[0],
                                            CAIXA_MANDANTE[1] + ALTURA_RECT * (i - 1),
                                            CAIXA_MANDANTE[2], CAIXA_MANDANTE[3]], 1)

            primitivas.rect(CINZA_ESCURO2, [CAIXA_MANDANTE[0] + 1,
                                            CAIXA_MANDANTE[1] + ALTURA_RECT * (i - 1) + 1,
                                            CAIXA_MANDANTE[2] - 2, CAIXA_MANDANTE[3] - 2])

            texto.escrever('X', [CAIXA_MANDANTE[0] + 31,
                            CAIXA_MANDANTE[1] + ALTURA_RECT * (i - 1)])

            primitivas.rect(PRETO, [CAIXA_VISITANTE[0],
                                            CAIXA_VISITANTE[1] + ALTURA_RECT * (i - 1),
                                            CAIXA_VISITANTE[2], CAIXA_VISITANTE[3]], 1)

            primitivas.rect(CINZA_ESCURO2, [CAIXA_VISITANTE[0] + 1,
                                            CAIXA_VISITANTE[1] + ALTURA_RECT * (i - 1) + 1,
                                            CAIXA_VISITANTE[2] - 2, CAIXA_VISITANTE[3] - 2])


    #Contornos dos confrontos
    primitivas.rect(PRETO, [POSX_CONFRONTOS, POSY_CONFRONTOS + ALTURA_RECT,
                                        LARGURA_RECT, ALTURA_RECT * qtd_confrontos], 1)

    primitivas.rect(PRETO, [POSX_CONFRONTOS, POSY_CONFRONTOS,
                                        LARGURA_RECT, ALTURA_RECT], 1)

    primitivas.rect(PRETO, SETA_AVANCO, 1)

    primitivas.rect(PRETO, SETA_RETORNO, 1) 


    #Caixas de salvar e de não salvar
    primitivas.rect(AZUL, CAIXA_SALVAR)
    primitivas.rect(PRETO, CAIXA_SALVAR, 1)
    texto.centralizado(CAIXA_SALVAR, "Sair e salvar")

    primitivas.rect(LARANJA, CAIXA_N_SALVAR)
    primitivas.rect(PRETO, CAIXA_N_SALVAR, 1)
    texto.centralizado(CAIXA_N_SALVAR, "Sair e não salvar")


#Desenha linhas de delimitação dos atributos
def desenharLinhas():
    largura_atributo = (RECT_ATRIBUTOS_TIMES[2] / 8)
    for i in range(8):
        primitivas.linha([RECT_ATRIBUTOS_TIMES[0] + largura_atributo * i, CLASSIFICACAO[1]],
            [RECT_ATRIBUTOS_TIMES[0] + largura_atributo * i, CLASSIFICACAO[1] + ALTURA_RECT * qtd_times - 2])


#Desenha os times na tabela de classificação 
#Desenha os atributos dos times
#'cor' é a cor da fonte
def desenharClassificacao():
    times = Simulador.times

    cor = PRETO

    desenharLinhas()

    for i in range(len(times)):

        #Nome
        texto.escrever(times[i].nome, [POSX_CLUBE, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #Pontuação
        texto.escrever(str(times[i].pontuacao), [RECT_ATRIBUTOS_TIMES[0] + 6, 
                        CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #Jogos
        texto.escrever(str(times[i].jogos), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + RECT_ATRIBUTOS_TIMES[2]/8, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #Vitórias
        texto.escrever(str(times[i].vitorias), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 2 * RECT_ATRIBUTOS_TIMES[2]/8, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #Empates
        texto.escrever(str(times[i].empates), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 3 * RECT_ATRIBUTOS_TIMES[2]/8, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #Derrotas
        texto.escrever(str(times[i].derrotas), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 4 * RECT_ATRIBUTOS_TIMES[2]/8, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #GP
        texto.escrever(str(times[i].gp), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 5 * RECT_ATRIBUTOS_TIMES[2]/8, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #GC
        texto.escrever(str(times[i].gc), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 6 * RECT_ATRIBUTOS_TIMES[2]/8, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)

        #Saldo de gols
        texto.escrever(str(times[i].saldoGols()), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 7 * RECT_ATRIBUTOS_TIMES[2]/8, CLASSIFICACAO[1] + ALTURA_RECT * i + 2], cor)


#Desenha a rodada com os times mandantes à esquerda e os times 
#visitantes à direita. 
def desenharRodada():
    rodada = Simulador.rodada
    times = Simulador.times

    texto_rodada = str(rodada) + 'ª RODADA'

    texto.centralizado([POSX_CONFRONTOS, POSY_CONFRONTOS, LARGURA_RECT, ALTURA_RECT], texto_rodada)

    indice = qtd_times * (rodada - 1)

    #Desenhar nomes dos times mandantes
    for i in range(0, qtd_times, 2):
        rect = [POSX_CONFRONTOS, POSY_CONFRONTOS + ALTURA_RECT * int(i/2 + 1), LARGURA_RECT, ALTURA_RECT]
        texto.alinhado(rect, times_em_ordem[confrontos[indice + i]])

    #Desenhar nomes dos times visitantes
    for i in range(1, qtd_times, 2):
        rect = [POSX_CONFRONTOS, POSY_CONFRONTOS + ALTURA_RECT * int(i/2 + 1), LARGURA_RECT, ALTURA_RECT]
        texto.alinhado(rect, times_em_ordem[confrontos[indice + i]], 'dir')

    desenharResultados()


#Desenha os resultados das partidas em determinada rodada dentro das
#caixas de resultados. Rodada começa em 1
def desenharResultados():
    rodada = Simulador.rodada

    indice = (rodada - 1) * qtd_times

    caixa = Operacoes.criarVetor(CAIXA_MANDANTE, 4)

    for i in range(int(qtd_times / 2)):
        caixa[0] = CAIXA_MANDANTE[0]

        texto.centralizado(caixa, Memoria.resultados[indice])
        indice += 1

        caixa[0] = CAIXA_VISITANTE[0]

        texto.centralizado(caixa, Memoria.resultados[indice])
        indice += 1

        caixa[1] += ALTURA_RECT


#Desenha o gol digitado pelo usuário em determinada caixa
#'key' é o botão pressionado pelo usuário
def desenharResultado(key):
    if interface.getInserir() == True:

        caixa = interface.getCaixa()

        indice = getIndiceCaixa(caixa)

        golSalvo = Memoria.getGol(indice)

        gol = ''
        
        if key == pygame.K_0:
            salvarGol(golSalvo, '0', indice, caixa)

        elif key == pygame.K_1:
            salvarGol(golSalvo, '1', indice, caixa)

        elif key == pygame.K_2:
            salvarGol(golSalvo, '2', indice, caixa)

        elif key == pygame.K_3:
            salvarGol(golSalvo, '3', indice, caixa)

        elif key == pygame.K_4:
            salvarGol(golSalvo, '4', indice, caixa)

        elif key == pygame.K_5:
            salvarGol(golSalvo, '5', indice, caixa)

        elif key == pygame.K_6:
            salvarGol(golSalvo, '6', indice, caixa)

        elif key == pygame.K_7:
            salvarGol(golSalvo, '7', indice, caixa)

        elif key == pygame.K_8:
            salvarGol(golSalvo, '8', indice, caixa)

        elif key == pygame.K_9:
            salvarGol(golSalvo, '9', indice, caixa)


#Verifica se o clique do mouse ocorreu sobre determinado botão e efetua
#as ações necessárias
def clique(posicao):
    rodada = Simulador.rodada

    caixa = []

    #Clique na região das caixas de resultados
    if(Operacoes.inRectangle(posicao, REGIAO_RESULTADOS)):
        caixa = Operacoes.criarVetor(CAIXA_MANDANTE, 4)

        #verifica se clique ocorreu dentro de alguma caixa
        caixa = Operacoes.inOneRectangle(posicao, caixa, [CAIXA_VISITANTE[0] - CAIXA_MANDANTE[0],
                                            ALTURA_RECT, 2, qtd_confrontos])

        #Clique ocorreu em uma caixa de resultado
        if(caixa != []):
            interface.setInserir(True)
            interface.setCaixa(caixa)
            primitivas.destacarRect(AMARELO, caixa)
            indice = getIndiceCaixa(caixa)  

            #desfaz resultado anterior, se houver
            if indice not in Simulador.indices:
                Simulador.desfazerResultado(indice) 

            #resultado anterior é descartado
            Memoria.setGol(indice, '  ')
                
        return 1

    #Atualizar classificação (se possível) com novo resultado
    if interface.getInserir() == True and caixa == []:
        interface.setInserir(False)
        apagarResultados()
        desenharResultados()
        Simulador.atualizar()
        Simulador.clearIndices()
        apagarClassificacao()
        desenharClassificacao()
        return 1

    #Clique na seta de avanço
    if(Operacoes.inRectangle(posicao, SETA_AVANCO)):
    
        if(rodada < qtd_rodadas):
            Simulador.rodada += 1
            apagarRodada()
            desenharRodada()
            
        return 1

    #Clique na seta de retorno
    if(Operacoes.inRectangle(posicao, SETA_RETORNO)):

        if(rodada > 1):
            Simulador.rodada -= 1
            apagarRodada()
            desenharRodada()
            
        return 1

    #Clique na caixa de salvar
    if(Operacoes.inRectangle(posicao, CAIXA_SALVAR)):
        Memoria.salvarClassificacao(Simulador.times)
        Memoria.formatarArquivo()
        return -1

    #Clique na caixa de não salvar
    if(Operacoes.inRectangle(posicao, CAIXA_N_SALVAR)):
        return -1

    return 1
         

#Apaga os times, os resultados e o número da rodada
def apagarRodada():

    for i in range(qtd_confrontos + 1):
        if i == 0:
           primitivas.rect(CINZA_ESCURO1, [POSX_CONFRONTOS + SETA_AVANCO[2] + 1, POSY_CONFRONTOS + 1,
                                                 LARGURA_RECT - 2 * SETA_AVANCO[2] - 1, ALTURA_RECT - 2])
        else:
            if i % 2 == 0:
                primitivas.rect(CINZA_ESCURO1, [POSX_CONFRONTOS + 1, POSY_CONFRONTOS + ALTURA_RECT * i + 1,
                                                   CAIXA_MANDANTE[0] - POSX_CONFRONTOS - 2, ALTURA_RECT - 2])
                primitivas.rect(CINZA_ESCURO1, [CAIXA_VISITANTE[0] + CAIXA_VISITANTE[2] + 1,
                                                      POSY_CONFRONTOS + ALTURA_RECT * i + 1,
                                                      POSX_CONFRONTOS + LARGURA_RECT - CAIXA_VISITANTE[0] - 
                                                      CAIXA_VISITANTE[2] - 2, ALTURA_RECT - 2])
                                                    

            if i % 2 != 0:
                primitivas.rect(CINZA_CLARO, [POSX_CONFRONTOS + 1, POSY_CONFRONTOS + ALTURA_RECT * i + 1,
                                                   CAIXA_MANDANTE[0] - POSX_CONFRONTOS - 2, ALTURA_RECT - 2])
                primitivas.rect(CINZA_CLARO, [CAIXA_VISITANTE[0] + CAIXA_VISITANTE[2] + 1,
                                                      POSY_CONFRONTOS + ALTURA_RECT * i + 1,
                                                      POSX_CONFRONTOS + LARGURA_RECT - CAIXA_VISITANTE[0] - 
                                                      CAIXA_VISITANTE[2] - 2, ALTURA_RECT - 2])
    apagarResultados()


#Apaga os resultados dos confrontos
def apagarResultados():
    rect = CAIXA_MANDANTE

    for i in range(qtd_confrontos):
        primitivas.destacarRect(CINZA_ESCURO2, rect)
        rect = Operacoes.mudarIndice(rect, 1, rect[1] + ALTURA_RECT)

    rect = CAIXA_VISITANTE

    for i in range(qtd_confrontos):
        primitivas.destacarRect(CINZA_ESCURO2, rect)
        rect = Operacoes.mudarIndice(rect, 1, rect[1] + ALTURA_RECT)


#Apaga os dados visualizados da classificação
def apagarClassificacao():
    times = Simulador.times

    for i in range(len(times)):

        if i % 2 == 0:
            cor = CINZA_ESCURO1
        else:
            cor = CINZA_ESCURO2

        rect = [POSX_CLUBE, CLASSIFICACAO[1] + ALTURA_RECT * i + 1,
                APAGAR_CLUBE[0], APAGAR_CLUBE[1]]

        primitivas.rect(cor, rect)


#Analisa um evento e efetua a ação necessária
def analisarEvento(sair):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #salva por default
            Memoria.salvarClassificacao(Simulador.times)
            Memoria.formatarArquivo()
            return -1

        if event.type == pygame.MOUSEBUTTONDOWN:
            return clique(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            desenharResultado(event.key)
            return 1

    return 1


#Retorna o índice de um time na lista confrontos de acordo com a caixa
#de resultado selecionada pelo usuário
def getIndiceCaixa(caixa):

    rodada = Simulador.rodada

    posicao = Operacoes.subtrairVetor(caixa, [CAIXA_MANDANTE[0], CAIXA_MANDANTE[1]])

    posicao = Operacoes.dividirVetor(posicao, [CAIXA_VISITANTE[0] - CAIXA_MANDANTE[0],
                                                  ALTURA_RECT])    

    return 2 * posicao[1] + posicao[0] + (rodada - 1) * qtd_times


#Salva algarismo digitado pelo usuário (gol) na lista resultados
#Um resultado pode ter no máximo 2 algarismos (Ex: time A 99 x 99 time B)
def salvarGol(golSalvo, gol, indice, caixa):
    if len(golSalvo) == 2 and golSalvo != '  ':
        return

    Simulador.pushIndice(indice)

    if len(golSalvo) == 1:
        primitivas.destacarRect(AMARELO, caixa)
        gol = golSalvo + gol
  
    texto.centralizado(caixa, gol)
    Memoria.setGol(indice, gol)