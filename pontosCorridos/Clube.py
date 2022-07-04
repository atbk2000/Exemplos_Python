
class Clube(object):
    """Clube e seus atributos"""
    nome = ''
    pontuacao = 0
    jogos = 0
    vitorias = 0
    empates = 0
    derrotas = 0
    gp = 0
    gc = 0
    #Posição do time na tabela considerando ordem alfabética
    posAlf = 0
    #Guarda os últimos resultados do time: V (vitória), E (empate), D (derrota)
    resultados = ''

    def __init__(self, Nome, Pontuacao, Jogos, Vitorias, Empates, Derrotas, GP, GC, posAlf):
        self.nome = Nome
        self.pontuacao = Pontuacao
        self.jogos = Jogos
        self.vitorias = Vitorias
        self.empates = Empates
        self.derrotas = Derrotas
        self.gp = GP
        self.gc = GC
        self.posAlf = posAlf

    def saldoGols(self):
        return (self.gp - self.gc)


