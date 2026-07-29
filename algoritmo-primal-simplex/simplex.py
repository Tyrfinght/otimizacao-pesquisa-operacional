import numpy as np

def primal_simplex(matriz_A, vetor_recursos, vetor_custos):
    """
    Função que resolve o Método Primal Simplex a partir de um PPL na forma padrão.
    Espera-se que o problema já tenha uma base factível associada às últimas 'm' colunas.
    """
    m, n = matriz_A.shape
    # Inicialização da base factível (assumindo variáveis de folga no final da matriz)
    base_factivel = np.arange(n - m, n)
    
    iteracao = 1
    
    while True:
        # Extração das matrizes e vetores da base atual
        coeficientes_obj_base = vetor_custos[base_factivel]
        matriz_base = matriz_A[:, base_factivel]
        
        # Passo 1: Calcular valores das variáveis básicas (B * xb = b)
        variaveis_atuais_base = np.linalg.solve(matriz_base, vetor_recursos)
        
        # Passo 2 e 3: Cálculo do vetor lambda (multiplicador) e custos reduzidos
        # lambda_vetor = B^(-T) * cb
        lambda_vetor = np.linalg.solve(matriz_base.T, coeficientes_obj_base)
        custos_reduzidos = vetor_custos - np.dot(lambda_vetor, matriz_A)
        
        # Condição de Parada A: Todos os custos reduzidos >= 0 (Ótimo encontrado)
        # Como as operações em ponto flutuante podem gerar -0.00000001, usamos uma tolerância (1e-8)
        if np.all(custos_reduzidos >= -1e-8):
            z_otimo = np.dot(coeficientes_obj_base, variaveis_atuais_base)
            
            # Reconstruir vetor x completo
            x_otimo = np.zeros(n)
            x_otimo[base_factivel] = variaveis_atuais_base
            
            return x_otimo, z_otimo
        
        # Passo 3 (continuação): Seleção da variável que ENTRA na base
        entering_var = np.argmin(custos_reduzidos)
        
        # Passo 4: Calcular a direção simplex (B * d = an)
        direcao = np.linalg.solve(matriz_base, matriz_A[:, entering_var])
        
        # Condição de Parada B: Se a direção for <= 0 para todo elemento, problema é ilimitado
        if np.all(direcao <= 1e-8):
            return "O problema é ilimitado.", None
            
        # Passo 5: Teste da razão para descobrir qual variável SAI da base (tamanho do passo)
        passos = np.where(direcao > 1e-8, variaveis_atuais_base / direcao, np.inf)
        exiting_var_idx_in_base = np.argmin(passos)
        
        # Passo 6: Atualizar a base
        base_factivel[exiting_var_idx_in_base] = entering_var
        iteracao += 1


# ==========================================
# TESTE DE EXECUÇÃO
# ==========================================
if __name__ == "__main__":
    # Exemplo simples de teste:
    # Min -3x1 - 2x2
    # s.t: x1 + x2 + x3 = 4
    #      x1 - x2 + x4 = 2
    # x >= 0
    
    A = np.array([
        [1,  1,  1,  0],
        [1, -1,  0,  1]
    ], dtype=float)
    b = np.array([4, 2], dtype=float)
    c = np.array([-3, -2, 0, 0], dtype=float) # Minimização
    
    print("Iniciando otimização Primal Simplex...\n")
    resultado_x, resultado_z = primal_simplex(A, b, c)
    
    if resultado_z is not None:
        print("--- SOLUÇÃO ÓTIMA ENCONTRADA ---")
        print(f"Vetor de Decisão (x): {np.round(resultado_x, 4)}")
        print(f"Valor Ótimo (Z): {round(resultado_z, 4)}")
    else:
        print(f"--- ERRO ---")
        print(resultado_x)

"""
==========================================
RESULTADO ESPERADO 
==========================================
Iniciando otimização Primal Simplex...

--- SOLUÇÃO ÓTIMA ENCONTRADA ---
Vetor de Decisão (x): [3. 1. 0. 0.]
Valor Ótimo (Z): -11.0
"""