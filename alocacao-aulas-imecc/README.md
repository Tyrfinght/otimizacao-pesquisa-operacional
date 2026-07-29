# Otimização de Escala e Alocação de Recursos (Caso: IMECC-Unicamp)

## Problema 
A alocação eficiente de capital humano é um dos maiores desafios operacionais em grandes instituições. Neste projeto, modelei o cenário real de atribuição de aulas do Instituto de Matemática, Estatística e Computação Científica (IMECC) da Unicamp. 
O objetivo foi desenvolver um modelo de otimização capaz de designar dezenas de professores para dezenas de disciplinas, respeitando restrições rígidas de horários, disponibilidade de salas, preferências individuais e limites de carga horária.

## Ferramentas e Métodos
* **Linguagem:** Python
* **Biblioteca:** PuLP (Linear/Integer Programming)
* **Método:** Programação Linear Inteira (Modelagem Matemática)

## Modelagem Matemática
O problema foi estruturado utilizando variáveis de decisão binárias e um conjunto de restrições operacionais e lógicas. 

**Função Objetivo:**
Maximizar a satisfação global da alocação, baseada numa matriz de preferência dos professores multiplicada pelo peso/importância da matéria:
`MAX Σ (α * PREF[p,m] + β * IMPORTANCIA[m]) * X[p,m,h]`

**Restrições Implementadas:**
1. **Unicidade:** Cada matéria deve ser atribuída a exatamente um professor em um horário específico.
2. **Limite de Carga:** Um professor não pode exceder o limite `k` de matérias atribuídas.
3. **Conflito de Horários:** Um professor não pode ser alocado em duas matérias simultâneas (mesmo horário).
4. **Disponibilidade de Salas:** O número de matérias alocadas em um horário `h` não pode exceder o número de salas físicas disponíveis.
5. **Blocos de Dias:** Restrição para alinhar as aulas aos blocos de dias da universidade (Ex: Seg/Qua/Sex ou Ter/Qui).

## Resultados e Conclusão
O modelo base conseguiu distribuir com sucesso as turmas, demonstrando a eficácia do *Course Assignment Model*. Em simulações mais complexas adicionando a variável tridimensional de horários e salas físicas, identificou-se que a sensibilidade dos parâmetros de entrada (como o limite irreal de disponibilidade) pode inviabilizar a solução, provando que a otimização de *Timetabling* exige dados altamente governados.

Esse tipo de modelagem é diretamente escalável para:
* Escalas de funcionários no varejo ou hospitais.
* Alocação de ativos e portfólios no mercado financeiro.
* Roteirização logística.

A documentação detalhada deste projeto, incluindo a justificativa matemática das variáveis, as matrizes de preferência originais e a análise crítica das falhas de alocação de salas, pode ser consultada no relatório oficial:
👉 **[Ler o Relatório Técnico (PDF)](./alocacao-aulas-imecc.pdf)**
