import random
import numpy as np


# ============================================================
#  Simulação do Problema dos 100 Prisioneiros
# ============================================================

def simular_prisioneiro(permutacao, prisioneiro_id):
    """
    Simula um prisioneiro seguindo a estratégia do loop:
    - Começa pela caixa com seu número
    - Segue a permutação abrindo no máximo 50 caixas
    """
    caixa_atual = prisioneiro_id
    for _ in range(50):
        conteudo = permutacao[caixa_atual - 1]
        if conteudo == prisioneiro_id:
            return True
        caixa_atual = conteudo
    return False


def fitness_prisioneiros(permutacao):
    """
    Fitness = número de prisioneiros que encontram seus números.
    Retorna valor entre 0 e 100.
    """
    sucesso = 0
    for prisioneiro in range(1, 101):
        if simular_prisioneiro(permutacao, prisioneiro):
            sucesso += 1
    return sucesso  # no GA maximizar é melhor


# ============================================================
#  Algoritmo Genético Especializado em Permutações
# ============================================================

class AlgoritmoGeneticoPrisioneiros:
    """
    Algoritmo genético especializado para o problema dos 100 prisioneiros.
    Cada indivíduo é uma permutação de 1..100 representando a configuração das caixas.
    """

    def __init__(self, funcao_de_fitness, 
                 tamanho_populacao: int = 200,
                 chance_de_mutacao: float = 0.02,
                 chance_de_cruzamento: float = 0.8,
                 quantidade_melhores: int = 20,
                 quantidade_de_geracoes: int = 300):

        self._funcao_de_fitness = funcao_de_fitness
        self._tamanho_populacao = tamanho_populacao
        self._chance_de_mutacao = chance_de_mutacao
        self._chance_de_cruzamento = chance_de_cruzamento
        self._quantidade_melhores = quantidade_melhores
        self._quantidade_de_geracoes = quantidade_de_geracoes

        self._N = 100  # número fixo para o problema


    # ---------------------------------------------------------
    # Execução principal
    # ---------------------------------------------------------

    def rodar(self):
        """ Executa o GA e retorna o melhor indivíduo encontrado. """
        
        self._gera_populacao_inicial()

        for _ in range(self._quantidade_de_geracoes):
            self._selecao_e_reproducao()

        return self._ordenar_por_aptidao()[0]


    # ---------------------------------------------------------
    # Inicialização
    # ---------------------------------------------------------

    def _gera_populacao_inicial(self):
        """ Gera a população inicial como permutações aleatórias. """

        self._populacao = []
        for _ in range(self._tamanho_populacao):
            individuo = list(range(1, self._N + 1))
            random.shuffle(individuo)
            self._populacao.append(individuo)


    # ---------------------------------------------------------
    # Avaliação
    # ---------------------------------------------------------

    def _ordenar_por_aptidao(self):
        """ Avalia todos e retorna ordenado do melhor para o pior. """

        avaliacoes = [
            {'individuo': ind, 'aptidao': self._funcao_de_fitness(ind)}
            for ind in self._populacao
        ]

        # ordenar por aptidão decrescente (quanto mais prisioneiros salvam, melhor)
        avaliacoes.sort(key=lambda x: x['aptidao'], reverse=True)

        return [a['individuo'] for a in avaliacoes]


    # ---------------------------------------------------------
    # Seleção + Reprodução
    # ---------------------------------------------------------

    def _selecao_e_reproducao(self):
        """ Gera a próxima geração. """

        # elitismo
        nova_pop = self._ordenar_por_aptidao()[: self._quantidade_melhores]

        # reprodução até encher a população
        while len(nova_pop) < self._tamanho_populacao:
            pai1, pai2 = random.choices(nova_pop, k=2)

            if np.random.random() < self._chance_de_cruzamento:
                filho = self._cruzamento(pai1, pai2)
            else:
                filho = pai1.copy()

            self._mutacao(filho)
            nova_pop.append(filho)

        self._populacao = nova_pop


    # ---------------------------------------------------------
    # Operadores Genéticos
    # ---------------------------------------------------------

    def _mutacao(self, individuo):
        """ Mutação por troca de posições (swap mutation). """

        if np.random.random() <= self._chance_de_mutacao:
            i, j = random.sample(range(self._N), 2)
            individuo[i], individuo[j] = individuo[j], individuo[i]

        return individuo


    def _cruzamento(self, pai1, pai2):
        """
        Cruzamento PMX (Partially Mapped Crossover), adequado para permutações.
        """

        tamanho = len(pai1)

        inicio = random.randint(0, tamanho - 2)
        fim = random.randint(inicio + 1, tamanho - 1)

        filho = [None] * tamanho

        # copia o meio do pai1
        filho[inicio:fim] = pai1[inicio:fim]

        # completa com elementos do pai2 mantendo permutação válida
        for x in pai2:
            if x not in filho:
                idx = filho.index(None)
                filho[idx] = x

        return filho


# ============================================================
#  Exemplo de uso (opcional)
# ============================================================

if __name__ == "__main__":

    ga = AlgoritmoGeneticoPrisioneiros(
        funcao_de_fitness=fitness_prisioneiros,
        tamanho_populacao=300,
        quantidade_melhores=30,
        quantidade_de_geracoes=200
    )

    melhor = ga.rodar()

    print("Melhor permutação encontrada:")
    print(melhor)
    print("Fitness:", fitness_prisioneiros(melhor))
