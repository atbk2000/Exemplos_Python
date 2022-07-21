import Interface.primitivas as primitivas
import Interface.limpar as limpar
import Operacoes
import pygame
import Interface.texto as texto
import Memoria
from Cadastro import *
from Simulador import Simul
from Interface.classe import interface


#Configura a imagem inicial que aparecerá ao usuário ao iniciar o programa
def inicializarGraficos(screen):
    interface.setSurface(screen)

    desenharFundo()

    desenharClassificacao()
    desenharRodada()

    from Cadastro import SETA_AVANCO, SETA_RETORNO

    primitivas.imagem('seta_retorno.png', [SETA_RETORNO[0] + 1, SETA_RETORNO[1] + 1])
    primitivas.imagem('seta_avanco.png', [SETA_AVANCO[0] + 1, SETA_AVANCO[1] + 1])




#Recebe um evento e decide qual ação deve efetuar
def analisarEvento(event, sair):
    if event.type == pygame.quit:
        sair = True
        return

    #Botão do mouse pressionado
    if event.type == pygame.MOUSEBUTTONDOWN:
        clique(pygame.mouse.get_pos())

    #Botão do teclado pressionado
    if event.type == pygame.KEYDOWN:
        desenharResultado(event.key)




#Verifica se o clique do mouse ocorreu sobre determinado botão e efetua
#as ações necessárias
def clique(posicao):
    rodada = Simul.getRodada()

    #Clique na seta de avanço
    if(Operacoes.dentro(posicao, SETA_AVANCO)):
    
        if(rodada < qtd_times - 1):
            Simul.setRodada(rodada + 1)
            limpar.rodada()
            desenharRodada()
            return

    #Clique na seta de retorno
    if(Operacoes.dentro(posicao, SETA_RETORNO)):

        if(rodada > 1):
            Simul.setRodada(rodada - 1)
            limpar.rodada()
            desenharRodada()
            return

    #Clique na região das caixas de resultados
    if(Operacoes.dentroIntervalo(CAIXA_MANDANTE[0], CAIXA_VISITANTE[0] + CAIXA_VISITANTE[2], posicao[0])):
        if(Operacoes.dentroIntervalo(CAIXA_MANDANTE[1], CAIXA_MANDANTE[1] + qtd_confrontos * ALTURA_RECT, posicao[1])):
      
            caixa = Operacoes.criarVetor(CAIXA_MANDANTE, 4)
            #verifica se clique ocorreu dentro de alguma caixa
            caixa = Operacoes.dentroAlgum(posicao, caixa, [CAIXA_VISITANTE[0] - CAIXA_MANDANTE[0],
                                             ALTURA_RECT, 2, qtd_confrontos])

            if(caixa != []):
                interface.setInserir(True)
                interface.setCaixa(caixa)
                primitivas.destacarCaixa(AMARELO, caixa)

            elif interface.getInserir() == True:
                interface.setInserir(False)
                limpar.resultados()
                desenharResultados()

    elif interface.getInserir() == True:
        interface.setInserir(False)
        limpar.resultados()
        desenharResultados()




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
            primitivas.rect(CINZA_ESCURO1, [POSX_CLASSIFICACAO, POSY_CLASSIFICACAO + ALTURA_RECT * i,
                                                    LARGURA_RECT, ALTURA_RECT])

        if i % 2 != 0:
            primitivas.rect(CINZA_ESCURO2, [POSX_CLASSIFICACAO, POSY_CLASSIFICACAO + ALTURA_RECT * i,
                                                    LARGURA_RECT, ALTURA_RECT])
  
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
    primitivas.rect(PRETO, [POSX_CLASSIFICACAO, POSY_CLASSIFICACAO, LARGURA_RECT,
                                        ALTURA_RECT * qtd_times], 1)

    #Desenhar os números indicadores de posição
    for i in range(qtd_times):
        texto.escrever(str(i + 1) + '.', [POSX_CLASSIFICACAO + 3, 
                                                    ALTURA_RECT * i + POSY_CLASSIFICACAO + 2])
   

    #Desenhar linhas de delimitação dos atributos
    largura_atributo = (RECT_ATRIBUTOS_TIMES[2] / 8)
    for i in range(8):
        primitivas.linha([RECT_ATRIBUTOS_TIMES[0] + largura_atributo * i, POSY_CLASSIFICACAO],
                        [RECT_ATRIBUTOS_TIMES[0] + largura_atributo * i, POSY_CLASSIFICACAO + ALTURA_RECT * qtd_times - 2])



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




#Desenha os times na tabela de classificação na ordem da lista 'times'
#Desenha também os atributos dos times
def desenharClassificacao():
    times = Simul.times

    for i in range(qtd_times):
        #Nome
        texto.escrever(times[i].nome, [POSX_CLASSIFICACAO + 25, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #Pontuação
        texto.escrever(str(times[i].pontuacao), [RECT_ATRIBUTOS_TIMES[0] + 6, 
                        POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #Jogos
        texto.escrever(str(times[i].jogos), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + RECT_ATRIBUTOS_TIMES[2]/8, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #Vitórias
        texto.escrever(str(times[i].vitorias), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 2 * RECT_ATRIBUTOS_TIMES[2]/8, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #Empates
        texto.escrever( str(times[i].empates), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 3 * RECT_ATRIBUTOS_TIMES[2]/8, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #Derrotas
        texto.escrever(str(times[i].derrotas), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 4 * RECT_ATRIBUTOS_TIMES[2]/8, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #GP
        texto.escrever(str(times[i].gp), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 5 * RECT_ATRIBUTOS_TIMES[2]/8, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #GC
        texto.escrever(str(times[i].gc), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 6 * RECT_ATRIBUTOS_TIMES[2]/8, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])

        #Saldo de gols
        texto.escrever(str(times[i].saldoGols()), [RECT_ATRIBUTOS_TIMES[0] + 6 
                        + 7 * RECT_ATRIBUTOS_TIMES[2]/8, POSY_CLASSIFICACAO + ALTURA_RECT * i + 2])




#Desenha a rodada com os times mandantes à direita e os times 
#visitantes à esquerda. 
def desenharRodada():
    rodada = Simul.getRodada()
    times = Simul.times

    texto_rodada = str(rodada) + 'ª RODADA'

    texto.centralizado([POSX_CONFRONTOS, POSY_CONFRONTOS, LARGURA_RECT, ALTURA_RECT], texto_rodada)

    indice = qtd_times * (rodada - 1)

    #Desenhar nomes dos times mandantes
    for i in range(0, qtd_times, 2):
        rect = [POSX_CONFRONTOS, POSY_CONFRONTOS + ALTURA_RECT * int(i/2 + 1), LARGURA_RECT, ALTURA_RECT]
        texto.alinhado(rect, times[confrontos[indice + i]].nome)

    #Desenhar nomes dos times visitantes
    for i in range(1, qtd_times, 2):
        rect = [POSX_CONFRONTOS, POSY_CONFRONTOS + ALTURA_RECT * int(i/2 + 1), LARGURA_RECT, ALTURA_RECT]
        texto.alinhado(rect, times[confrontos[indice + i]].nome, 'dir')

    desenharResultados()




#Desenha os resultados das partidas em determinada rodada dentro das
#caixas de resultados. Rodada começa em 1
def desenharResultados():
    rodada = Simul.getRodada()

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

        rodada = Simul.getRodada()

        caixa = interface.getCaixa()

        posicao = Operacoes.subtrairVetor(caixa, [CAIXA_MANDANTE[0], CAIXA_MANDANTE[1]])

        posicao = Operacoes.dividirVetor(posicao, [CAIXA_VISITANTE[0] - CAIXA_MANDANTE[0],
                                                  ALTURA_RECT])    

        indice = 2 * posicao[1] + posicao[0] + (rodada - 1) * qtd_times
        
        if key == pygame.K_0:
            texto.centralizado(caixa, '0')
            Memoria.inserirResultado(indice, '0')

        elif key == pygame.K_1:
            texto.centralizado(caixa, '1')
            Memoria.inserirResultado(indice, '1')

        elif key == pygame.K_2:
            texto.centralizado(caixa, '2')
            Memoria.inserirResultado(indice, '2')

        elif key == pygame.K_3:
            texto.centralizado(caixa, '3')
            Memoria.inserirResultado(indice, '3')

        elif key == pygame.K_4:
            texto.centralizado(caixa, '4')
            Memoria.inserirResultado(indice, '4')

        elif key == pygame.K_5:
            texto.centralizado(caixa, '5')
            Memoria.inserirResultado(indice, '5')

        elif key == pygame.K_6:
            texto.centralizado(caixa, '6')
            Memoria.inserirResultado(indice, '6')

        elif key == pygame.K_7:
            texto.centralizado(caixa, '7')
            Memoria.inserirResultado(indice, '7')

        elif key == pygame.K_8:
            texto.centralizado(caixa, '8')
            Memoria.inserirResultado(indice, '8')

        elif key == pygame.K_9:
            texto.centralizado(caixa, '9')
            Memoria.inserirResultado(indice, '9')
