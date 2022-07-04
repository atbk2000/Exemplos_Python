
#Times participantes do campeonato
#Índices em ordem alfabética
times_em_ordem = ['América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 
                  'Bragantino','Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense',
                  'Fortaleza', 'Goiás', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Juventude' 
                  ]


qtd_times = int(len(times_em_ordem))
qtd_confrontos = int(qtd_times / 2)

 #Lista que contém a ordem dos confrontos, em ordem alfabética.
 #Por exemplo, time A... é o primeiro time em ordem alfabética,
 #logo recebe índice 0, time C... é o quarto, logo recebe índice 3.
 #A ocorrência ... 3, 0 ... indicaria uma partida em que o time C...
 #seria o mandante e o time A... o visitante.
confrontos = [12, 17, 2, 11, 16, 7, 9, 14, 3, 15, 5, 8, 13, 10, 18, 1, 4, 0, 19, 6,
              14, 16, 0, 19, 8, 4, 10, 12, 17, 9, 11, 18, 6, 2, 15, 13, 1, 3, 7, 5,
              6, 18, 1, 11, 12, 15, 16, 8, 3, 9, 17, 0, 19, 10, 2, 5, 4, 14, 13, 7,
              11, 16, 0, 1, 7, 6, 14, 3, 10, 2, 5, 19, 8, 13, 9, 12, 15, 4, 18, 17,
              3, 0, 1, 7, 11, 5, 16, 12, 2, 14, 6, 8, 17, 10, 19, 15, 13, 18, 4, 9,
              3, 2, 12, 1, 18, 10, 16, 6, 5, 13, 15, 8, 7, 11, 14, 17, 4, 19, 9, 0,
              0, 5, 11, 14, 6, 3, 8, 18, 17, 7, 19, 16, 13, 12, 2, 9, 10, 15, 1, 4,
              3, 4, 12, 11, 18, 7, 8, 0, 17, 16, 15, 2, 13, 19, 14, 6, 10, 1, 9, 5,
              0, 10, 11, 13, 6, 15, 16, 3, 5, 14, 19, 12, 7, 9, 2, 8, 4, 18, 1, 17,
              0, 7, 12, 3, 6, 11, 16, 5, 17, 15, 19, 1, 13, 14, 2, 4, 10, 8, 9, 18,
              8, 19, 3, 17, 12, 2, 10, 6, 15, 11, 18, 0, 14, 7, 9, 16, 13, 1, 5, 4,
              19, 17, 6, 9, 7, 3, 11, 10, 14, 15, 0, 12, 1, 8, 5, 18, 16, 2, 4, 13,
              10, 7, 17, 6, 3, 11, 8, 14, 9, 1, 15, 5, 13, 0, 2, 19, 12, 4, 18, 16,
              15, 9, 1, 6, 11, 0, 8, 17, 3, 13, 5, 12, 4, 16, 18, 19, 7, 2, 14, 10,
              12, 8, 19, 3, 17, 11, 7, 15, 16, 1, 4, 10, 2, 18, 0, 14, 9, 13, 6, 5,
              6, 4, 12, 7, 14, 1, 9, 19, 8, 11, 3, 18, 17, 2, 13, 16, 10, 5, 15, 0,
              2, 13, 1, 15, 11, 9, 4, 17, 7, 8, 19, 14, 18, 12, 5, 3, 0, 6, 16, 10,
              7, 4, 6, 13, 14, 12, 1, 2, 11, 19, 15, 18, 8, 9, 17, 5, 10, 3, 0, 16,
              18, 14, 5, 1, 4, 11, 12, 6, 16, 15, 19, 7, 3, 8, 2, 0, 13, 17, 9, 10]

qtd_rodadas = len(confrontos)/qtd_times

#Cores
VERDE = (0, 150, 150)
AMARELO = (255, 255, 170)
CINZA_ESCURO1 = (210, 210, 210)
CINZA_ESCURO2 = (200, 200, 200)
CINZA_CLARO = (220, 220, 220)
AZUL = (0, 230, 230)
LARANJA = (0, 204, 170)
PRETO = (0, 0, 0)

#Tamanho da tela
SCREEN_SIZE = [1100, 600]

ALTURA_RECT = 22
LARGURA_RECT = 480

POSX_CONFRONTOS = 10
POSY_CONFRONTOS = 10

#Caixas de resultados [POSX, POSY, LARGURA, ALTURA]
CAIXA_MANDANTE = [POSX_CONFRONTOS + (LARGURA_RECT / 2) - 10 - 25,
                 POSY_CONFRONTOS + 2 + ALTURA_RECT, 25, ALTURA_RECT - 4]
CAIXA_VISITANTE = [POSX_CONFRONTOS + (LARGURA_RECT / 2) + 10,
                  POSY_CONFRONTOS + 2 + ALTURA_RECT, 25,  ALTURA_RECT - 4]


#Região onde se encontram as caixas de resultados
REGIAO_RESULTADOS = [CAIXA_MANDANTE[0], CAIXA_MANDANTE[1], CAIXA_VISITANTE[0] + CAIXA_VISITANTE[2]
                         - CAIXA_MANDANTE[0], qtd_confrontos * ALTURA_RECT]


#Setas de avanço e retorno
SETA_RETORNO = [POSX_CONFRONTOS, POSY_CONFRONTOS, 35, ALTURA_RECT]
SETA_AVANCO = [POSX_CONFRONTOS + LARGURA_RECT - 35,
                   POSY_CONFRONTOS, 35, ALTURA_RECT]


#Largura disponível para acomodar o nome do clube na tabela de classificação
LARGURA_CLUBE = 250


#Dimensões da tabela de classificação
#[POSX, POSY, LARGURA]
CLASSIFICACAO = [500, 30, LARGURA_CLUBE + 2 * LARGURA_RECT / 3]


#Caixas que permitem ao usuário salvar ou não seu progresso
#[POSX, POSY, LARGURA, ALTURA]
CAIXA_SALVAR = [POSX_CONFRONTOS, CLASSIFICACAO[1] + (qtd_times - 1) * ALTURA_RECT,
                200, ALTURA_RECT]
CAIXA_N_SALVAR = [CAIXA_SALVAR[0] + CAIXA_SALVAR[2] + 30,
                   CAIXA_SALVAR[1], CAIXA_SALVAR[2], CAIXA_SALVAR[3]]


#Retângulo onde são atribuídos os pontos, as vitórias, as derrotas ... dos times
#Inserida acima da tabela de classificação
#[POSX, POSY, LARGURA]
RECT_ATRIBUTOS_TIMES = [CLASSIFICACAO[0] + LARGURA_CLUBE, POSX_CONFRONTOS, 2 * LARGURA_RECT / 3]


#Posição x onde o nome do clube aparece na tabela de classificação
POSX_CLUBE = CLASSIFICACAO[0] + 28


#Retângulo com dimensões para apagar o clube e seus atributos
#[largura, altura]
APAGAR_CLUBE = [CLASSIFICACAO[2] - 2 - 28, ALTURA_RECT - 2]



