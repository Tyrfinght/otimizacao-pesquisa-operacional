# Otimização de Trânsito e Fluxo em Redes (Case: Rodovia SP-065)

## Problema 
O congestionamento viário gera perdas incalculáveis de tempo e recursos na cadeia logística. Neste projeto, modelei a rede viária de um trecho de alto tráfego (Rodovia Dom Pedro I - SP-065) utilizando a Teoria dos Grafos. 
O objetivo foi identificar gargalos operacionais e testar quantitativamente, através de algoritmos de Fluxo Máximo (Max Flow), o impacto de intervenções de infraestrutura antes da execução de qualquer obra física.

## Ferramentas e Métodos
* **Linguagem:** Python
* **Biblioteca:** NetworkX (Modelagem de Grafos e Algoritmos de Redes)
* **Método:** Algoritmo de Fluxo Máximo, Teoria dos Grafos

## Modelagem Matemática
A via foi traduzida para um Grafo Direcionado `G = (V, A)`, onde os *Nós* representam interseções e os *Arcos* representam os trechos de rodovia, com capacidades calculadas em veículos/hora.

**Função Objetivo:**
Maximizar o escoamento total da rede, garantindo a conservação de fluxo nos nós intermediários.

Foi criado um script simulando três cenários:
1. **Cenário Base:** O modelo identificou estrangulamentos matemáticos exatos no acesso da marginal à pista principal (capacidade de 3.000 v/h) e nas saídas.
2. **Cenário de Intervenção de Entrada:** Simulação do impacto da duplicação da via de acesso.
3. **Cenário de Intervenção Completa:** Ajuste estendido das saídas para escoar o fluxo induzido.

## Relatório Técnico
A documentação completa com as equações matemáticas, mapas da modelagem e gráficos comparativos pode ser lida no arquivo [Projeto-MS529-173216-205577.pdf](./Projeto-MS529-173216-205577.pdf) anexo a este repositório.

## Limitações e Trabalhos Futuros
O modelo atual atua com condições ideais de escoamento. Para avançar para um ambiente de produção (Gêmeo Digital), os próximos passos envolvem:
* Inserção de estocasticidade (probabilidade de acidentes e chuvas).
* Inclusão de transporte de carga pesada (caminhões e restrições de frenagem).
* Integração do modelo com dados de GPS em tempo real.
