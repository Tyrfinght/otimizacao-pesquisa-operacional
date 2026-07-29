import networkx as nx

def calcular_fluxo_cenario(capacidade_3_4, capacidade_6_8, capacidade_7_9, nome_cenario):
    """
    Função para calcular o Fluxo Máximo na SP-065 variando os parâmetros de capacidade dos gargalos.
    """
    # Criação do grafo direcionado
    G = nx.DiGraph()

    # Adicionando os arcos e suas capacidades (veículos/hora)
    # Nó 0 é a super origem (s) e Nó 10 é o super destino (t)
    G.add_edge(0, 1, capacity=8000)
    G.add_edge(0, 2, capacity=12000)
    
    G.add_edge(1, 3, capacity=8000)
    G.add_edge(2, 4, capacity=12000)
    
    # Gargalo 1: Conexão Marginal -> Principal
    G.add_edge(3, 4, capacity=capacidade_3_4) 
    
    G.add_edge(4, 5, capacity=12000)
    G.add_edge(5, 6, capacity=7800)
    G.add_edge(5, 7, capacity=7800)
    
    # Gargalos 2 e 3: Saídas para a Rodovia Anhanguera
    G.add_edge(6, 8, capacity=capacidade_6_8) 
    G.add_edge(7, 9, capacity=capacidade_7_9) 
    
    G.add_edge(8, 10, capacity=float('inf'))
    G.add_edge(9, 10, capacity=float('inf'))

    # Calculando o fluxo máximo (Maximum Flow) usando os algoritmos nativos do NetworkX
    fluxo_maximo, fluxo_dict = nx.maximum_flow(G, 0, 10)
    
    print(f"--- {nome_cenario} ---")
    print(f"Fluxo Máximo Total Suportado: {fluxo_maximo} veículos/hora")
    print(f"-> Escoamento no trecho 3-4 (Marginal-Principal): {fluxo_dict[3][4]} v/h")
    print(f"-> Escoamento no trecho 6-8 (Saída 1): {fluxo_dict[6][8]} v/h")
    print(f"-> Escoamento no trecho 7-9 (Saída 2): {fluxo_dict[7][9]} v/h\n")

if __name__ == "__main__":
    # Simulação Cenário 1: Original (Gargalos limitados em 3000 v/h)
    calcular_fluxo_cenario(
        capacidade_3_4=3000, 
        capacidade_6_8=3000, 
        capacidade_7_9=3000, 
        nome_cenario="Cenário Original"
    )

    # Simulação Cenário 2: Duplicação do acesso (trecho 3-4 subindo para 6000 v/h)
    calcular_fluxo_cenario(
        capacidade_3_4=6000, 
        capacidade_6_8=3000, 
        capacidade_7_9=3000, 
        nome_cenario="Cenário 2: Duplicação do trecho 3-4"
    )

    # Simulação Cenário 3: Otimização Geral (todas as saídas suportando o fluxo de 6000 v/h)
    calcular_fluxo_cenario(
        capacidade_3_4=6000, 
        capacidade_6_8=6000, 
        capacidade_7_9=6000, 
        nome_cenario="Cenário 3: Otimização Geral (Acessos e Saídas)"
    )