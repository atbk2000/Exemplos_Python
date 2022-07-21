from Interface.classe import interface
import Simulador
import Interface.InterfaceSimul as InterfaceSimul
import Interface.Constantes as Constantes
import pygame
import Memoria
import Erros
import Operacoes

pygame.init()

Erros.verificaRodadas()

if Memoria.iniciar(Constantes.qtd_times) == 1:
    Simulador.inicializarTimes()
else:
    Simulador.times = Memoria.timesSalvos()


screen = pygame.display.set_mode(Constantes.SCREEN_SIZE)
InterfaceSimul.inicializarGraficos(screen)

sair = False
clock = pygame.time.Clock()

while not sair:

    #limitar o while loop a 10 vezes por segundo
    clock.tick(10)

    if(InterfaceSimul.analisarEvento(sair) == 1):
        pygame.display.flip()
    else:
        sair = True

pygame.quit()











  
    