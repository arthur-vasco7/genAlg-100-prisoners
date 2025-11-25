# Algoritmo Genético: Problema dos 100 prisioneiros
---

[documentação do projeto](https://drive.google.com/file/d/139lBUTI6KX-JT_SqhyYrGYrS-WFioTp0/view?usp=sharing)

## Entendendo o problema:

### Problema dos 100 prisoneiros:
Cada prisioneiro é enumerado de um a cem, assim como 100 caixas espalhadas em uma sala.
Cada caixa contém uma ficha com um número, também de 1 a 100, que representa um prisioneiro (fichas dispostas aleatoriamente). Um por vez, cada prisioneiro terá chance para abrir 50 caixas, deixando a sala com a mesma disposição inicial, e sem se comunicar com os outros. Caso alguma delas contenha o número que o representa, ele está liberado.

> Logo, escolhendo aleatoriamente, cada prisoneiro tem 50% de chance de encontrar seu número:

$$
\frac{50}{100} = \frac{1}{2} 
$$

No entanto, para que algum deles seja solto, é necessário que todos encontrem seus respectivos números, caso pelo menos um falhe, todos são executados. Ou seja, todos vencem ou todos perdem.

> Instintivamente, nossa primeira ideia seria multiplicar a probabilidade de um prisioneiro encontrar, pela quantidade total de prisioneiros:

$$
\frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \ldots = \left(\frac{1}{2}\right)^{100} 
$$

>Isso nos dá uma chance incompreensivelmente pequena, de aproximadamente: 

$$
7.886 \times 10^{-31} 
$$
>Não dá muita esperança aos prisioneiros. Existe alguma forma de aumentar as chances de vencer?

### Solução:

A melhor solução teórica para este problema consiste em fazer com que cada prisioneiro comece pela caixa que possui seu número na tampa, e então prossiga abrindo até que encontre a caixa que  o liberta ou as tentativas se esgotem. Se todos os 100 se organizem dessa forma, a chance de que todos sejam libertos cresce absurdamente para pouco mais 30%.

#### Por que?

Na descrição do problema, podemos perceber alguns fatos:
- Não existem caixas com números repetidos;
- Todas as caixas apontam para outra caixa no mesmo conjunto de elementos (1-100);
- Caixas podem conter seu próprio número.

Considerando o entre número exterior da caixa e número interior como uma função bijetora, podemos entender a disposição das caixas como uma ***permutação*** do conjunto original ordenado de 1 a 100.

> Permutação: Conceito matemático entendido como uma bijeção de um conjunto finito em si mesmo, onde cada elemento aparece exatamente uma vez (lista ordenada sem repetições). Pode ser representada como uma série de ciclos disjuntos onde cada cada ciclo descrevem como os elementos se movem entre si. 

Portanto, ao iniciar pelo número que o representa, o prisioneiro tem garantia de que aquele ciclo possuirá uma caixa que aponta para aquela caixa, e consequentemente, seu número. Sendo assim, cada indivíduo falha somente quando o ciclo é de tamanho maior que 50 (total de chances para abrir caixas).

>Linha 1: Entrada (Número na tampa da caixa)
>Linha 2: Resultado (Caixa a ser aberta no próximo passo)

$$
  a = 
  \begin{pmatrix}
    1 & 2 & 3 & \cdots & 99 & 100 \\
    19 & 38 & 47 & \cdots &  3  & 26
  \end{pmatrix}
$$

> No caso acima, consideramos uma grande permutação contendo todos os elementos, que seria o pior caso para os prisioneiros, visto que seriam necessárias 100 aberturas de caixas até encontrar o número desejado.

Dessa forma, a probabilidade de que os prisioneiros sejam libertos é a mesma de que uma permutação aleatória de 100 números **não** contenha um loop de tamanho maior que 50.

> Chance de um arranjo aleatório gerar um loop de tamanho 100:

$$
\frac{100!}{100} \div \frac{1}{100!} = \frac{1}{100}
$$

>Quantidade de loops distintos dividia pelo total de permutações.

>De forma análoga, a probabilidade de obter um loop de tamanho 99 equivale a 1/99, tamanho 98 = 1/98...
>Logo, a chance de existir um loop de tamanho superior a 50:

$$
\frac{1}{51} + \frac{1}{52} +\frac{1}{53} + \cdots+ \frac{1}{100} = 0.69
$$

>Assim, a chance de **não** existir um loop de tamanho superior a 50:

$$
1.00 - 0.69 = 0.31
$$

Note que cada indivíduo ainda tem apenas 50% de chance de encontrar seu número, já que so podem abrir 50 caixas de um total de 100. No entanto, a probabilidade de todos encontrarem suas caixas usando a estratégia do loop é de 31%, enquanto 69% das vezes menos de 50 acharão seu número.

### Algoritmo Genético:

Algoritmos genéticos usam de conceitos da biologia e da teoria da evolução para buscar respostas com maior taxa de acerto para problemas combinatórios, consistindo em:

- População de soluções possíveis (Geração 0 consistindo em soluções aleatórias);
- Fitness function: Avalia o quão boa uma solução é, baseada em métricas do problema;
- Seleção: Escolher as melhores soluções com base na fitness function;
- Cruzamento: Misturar trechos das soluções selecionadas para  construir uma nova geração;
- Mutação: Toque de aleatoriedade para garantir que novas soluções apareçam, a fim de evitar loops de gerações inferiores à anterior.

Esse processo é repetido até que a próxima geração esteja completa. A quantidade máxima de gerações (iterações) pode ser estabelecida, ou até que se encontre uma solução que satisfaça o propósito.



### Execução

* **Configuração do ambiente e execução do código principal**:

  1. Criar o ambiente virtual:

     ```bash
     python3 -m venv .venv
     ```
  2. Ativar o ambiente virtual:

     ```bash
     source .venv/bin/activate
     ```
  3. Instalar as dependências:

     ```bash
     pip install -r requirements.txt
     ```
  4. Executar o programa principal:

     ```bash
     python3 -m src.main
     ```

* **Executar a análise de tempo**:

  ```bash
  python3 -m src.analyze.time_analyse
  ```
