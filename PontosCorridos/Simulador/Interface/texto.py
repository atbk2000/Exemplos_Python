from Interface.classe import interface
import pygame


#Desenha um texto 'caracteres' na superfície 'Surface' nas cordenadas 'posicao'
def escrever(caracteres, posicao, cor = (0, 0, 0)):
    fonte = pygame.font.Font('Prototype.ttf', 16)

    texto = fonte.render(caracteres, False, cor)

    interface.getSurface().blit(texto, posicao)



#Centraliza 'texto' no centro do retângulo 'rect' e o desenha
def centralizado(rect, texto):
    fonte = pygame.font.Font('Prototype.ttf', 16)

    tamanho = fonte.size(texto)

    posX = rect[0] + (rect[2] - tamanho[0]) / 2
    posY = rect[1] + (rect[3] - tamanho[1]) / 2

    escrever(texto, [posX, posY])



#Alinha texto para a direita ou esquerda dentro de 'rect' e o desenha
def alinhado(rect, texto, alinhamento = 'esq'):
    fonte = pygame.font.Font('Prototype.ttf', 16)

    tamanho = fonte.size(texto)

    posY = rect[1] + (rect[3] - tamanho[1]) / 2

    if alinhamento == 'esq':
        posX = rect[0] + 5
        escrever(texto, [posX, posY])

    elif alinhamento == 'dir':
        posX = rect[0] + rect[2] - 5 - tamanho[0]
        escrever(texto, [posX, posY])
