

#Classe para a interface
class interface():

    __sur = None

    #Variável que indica se o usuário está digitando os resultados
    __inserir = False

    #Variável que indica última caixa selecionada pelo usuário
    #Lista com 4 elementos
    __caixa = []


    def setSurface(Surface):
        interface.__sur = Surface

    def setInserir(estado):
        interface.__inserir = estado

    def setCaixa(caixa):
        interface.__caixa = caixa


    def getSurface():
        return interface.__sur

    def getInserir():
        return interface.__inserir

    def getCaixa():
        return interface.__caixa


   
  
