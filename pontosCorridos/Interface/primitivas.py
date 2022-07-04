from Interface.classe import interface
import Operacoes
import pygame

#Destaca o retângulo 'rect' com uma cor 'cor'
def destacarRect(cor, Rect):
    retangulo = Operacoes.rectInterno(Rect)
    rect(cor, retangulo)



#Desenha retângulo
def rect(cor, rect, width = 0):
    pygame.draw.rect(interface.getSurface(), cor, rect, width)



#Desenha linha 
def linha(pos1, pos2):
    pygame.draw.line(interface.getSurface(), (0, 0, 0), pos1, pos2)



#Desenha a imagem no arquivo 'nome_arquivo' na superfície 'Surface' nas
#coordenadas 'posicao'
def imagem(nome_arquivo, posicao):
    imagem = pygame.image.load(nome_arquivo)

    interface.getSurface().blit(imagem, posicao)
