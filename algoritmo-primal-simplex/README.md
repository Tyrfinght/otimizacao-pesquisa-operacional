# Construção do Método Primal Simplex sem bibliotecas prontas

## Contexto
Solvers de otimização comerciais (como Gurobi, CPLEX ou funções do SciPy/PuLP) são caixas-pretas extremamente eficientes. No entanto, para atuar na modelagem matemática em alto nível, é fundamental entender o motor algébrico que resolve os problemas de Programação Linear.
Neste projeto, implementei o clássico **Algoritmo Primal Simplex** do zero, utilizando apenas álgebra linear matricial para solucionar Problemas de Programação Linear (PPL) na forma padrão.

## Ferramentas e Métodos
* **Linguagem:** Python
* **Biblioteca Matemática:** NumPy
* **Método:** Primal Simplex (Matricial)

## Lógica do Algoritmo
O script resolve PPLs de minimização restritos a `Ax = b` e `x >= 0`. O algoritmo foi estruturado nos 7 passos clássicos da Pesquisa Operacional:
1. Extração do sistema linear da base factível (`B * xb = b`).
2. Cálculo do multiplicador do simplex/variáveis duais (`B' * λ = cb`).
3. Verificação dos custos reduzidos das variáveis não-básicas (`cn - λ' * an`).
4. Identificação da variável que entra na base (direção simplex: `B * d = an`).
5. Teste da razão mínima (tamanho do passo `xb / d`) para determinar a variável que sai.
6. Atualização iterativa da partição básica.
7. Verificação das condições de parada (Solução Ótima encontrada ou Problema Ilimitado).

## Relatório e Documentação Teórica
A dedução algébrica das passagens e o relatório completo do projeto podem ser acessados aqui:
**[Ler o Relatório (PDF)](./Proj-MS428_173216.pdf)**
