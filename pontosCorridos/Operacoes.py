import math
#Arquivo responsável pela implementação de funções lógicas e aritméticas

#Verifica se um número está dentro de um intervalo fechado
def inInterval(limInferior, limSuperior, numero):
    if (numero >= limInferior and numero <= limSuperior): 
        return True
    return False


#Verifica se as coordenadas de posicao estão dentro de um 
#retângulo. Retorna True caso estiver, False caso contrário
def inRectangle(posicao, retangulo):
    if(inInterval(retangulo[0], retangulo[0] + retangulo[2], posicao[0])):
        if(inInterval(retangulo[1], retangulo[1] + retangulo[3], posicao[1])):
            return True
    return False


#Verifica se as coordenadas de 'posicao' estão dentro de
#algum retângulo dentre certos retângulos a serem verificados
#delta = [dx, dy, iteraçõesX, iteracõesY].
def inOneRectangle(posicao, rect, delta):

    pos_inicial_Y = rect[1]

    for i in range(delta[2]):
        for j in range(delta[3]):

            if(inRectangle(posicao, rect)):
                return rect

            rect[1] = rect[1] + delta[1]

        rect[1] = pos_inicial_Y        
        rect[0] = rect[0] + delta[0]
    
    return []


#Retorna o retângulo dentro do retângulo 'rect'
def rectInterno(rect):
    return [rect[0] + 1, rect[1] + 1, rect[2] - 2, rect[3] - 2]


#Cria um vetor igual a 'vetor' até o índice 'n'
def criarVetor(vetor, n):
    vet = []
    for i in range(n):
        vet.append(vetor[i])
    return vet


#Cria um novo vetor modificando 'vetor', alternando o índice 'indice'
#por um novo valor 'val'
def mudarIndice(vetor, indice, val):
    if (indice < 0 or indice >= len(vetor)):
        raise "Index out of range"
        return
    else:
        vetor = criarVetor(vetor, len(vetor))
        vetor[indice] = val
        return vetor


#Retira o caracter no índice 'index' da string 'string'
def pop(string, index):
    if index < (len(string) - 1):
        return string[:index] + string[(index + 1):]
    return string[:index]


#Transforma uma string em um número inteiro
#Ex: '1025' -> 1025. Primeiro exclui todos os caracteres
#não numéricos presentes na string. Ex: '10ab9' -> '109'
def stringToInt(str):
    numero = 0
    peso = 0

    for i in range(len(str)):
        algarismo = ord(str[i]) - 48

        if not inInterval(0, 9, algarismo):
            str = pop(str, i)

    for i in range(len(str) - 1, -1, -1):

        numero += (ord(str[i]) - 48) * math.pow(10, peso)
        peso += 1

    return int(numero)


#Retorna a ordem de grandeza de um número
def grandeza(numero):
    ordem = 1

    while(numero >= 10):
        ordem += 1
        numero /= 10

    return ordem


#Divide um vetor 2D 'vetor' pelo 'divisor'
def dividirVetor(vetor, divisor):
    return [int(vetor[0] / divisor[0]), int(vetor[1] / divisor[1])]


#Subtrai um vetor 2D 'vetor' pelo 'subtraendo'
def subtrairVetor(vetor, subtraendo):
    return [int(vetor[0] - subtraendo[0]), int(vetor[1] - subtraendo[1])]





