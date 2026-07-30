# Otimização Não-Linear: Análise de Convergência 

## O Projeto
Encontrar o ponto de mínimo global em funções não-lineares complexas é o motor que treina as Redes Neurais modernas. Este projeto foca na implementação e no *benchmarking* de três algoritmos clássicos de otimização irrestrita, avaliando seu custo computacional, eficiência e sensibilidade ao ponto inicial.

## Métodos Implementados
* **Gradiente Descendente:** Avanço iterativo baseado na direção de maior declive da função (gradiente negativo).
* **Método de Newton:** Utiliza derivadas de segunda ordem (Hessiana) para saltos mais precisos e convergência quadrática.
* **Método da Secante:** Alternativa *quasi-Newton* que aproxima a derivada usando diferenças finitas.

## Teste de Estresse
Os algoritmos foram testados contra funções matemáticas multivariáveis desenhadas especificamente para confundir otimizadores (múltiplos mínimos locais e vales planos):
1. Função Quadrática 
2. Função de Rosenbrock (O clássico problema do "Vale")
3. Função de Rastrigin (Altamente multimodal)
4. Função de Styblinski-Tang

## Resultados Críticos
* O **Método de Newton** convergiu com maestria na Função de Rosenbrock (poucas iterações), desde que o ponto inicial não causasse singularidade na Hessiana.
* O **Gradiente Descendente** penalizou severamente o custo computacional com passos lentos, exigindo milhares de iterações, confirmando a necessidade de algoritmos adaptativos (como Adam) em cenários reais.
* Aumentar o rigor da tolerância (de `1e-7` para `1e-14`) quase dobrou as iterações do Método de Newton, provando que a precisão de máquina tem um custo linear em otimização.

## Código Fonte e Relatório
O script em Python e as análises gráficas do comportamento convergente estão documentados abaixo:
👉 **[Ler o Relatório (PDF)](./Projeto_Computacional_MS629_2S-2023.pdf)**
