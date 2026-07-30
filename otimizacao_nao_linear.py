import numpy as np

def metodo_newton(f, df, x0, epsilon=1e-7, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raízes de f(x).
    Requer a função original f(x) e sua derivada primeira df(x).
    """
    x = x0
    for n in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            print("Erro: Derivada igual a zero. O método falhou.")
            return None
            
        x_novo = x - (fx / dfx)
        
        if abs(x_novo - x) <= epsilon or abs(f(x_novo)) <= epsilon:
            print(f"[Newton] Convergiu em {n} iterações. Raiz: {x_novo:.8f}")
            return x_novo
            
        x = x_novo
        
    print("[Newton] Máximo de iterações atingido. Não convergiu.")
    return None


def metodo_secante(f, x0, x1, epsilon=1e-7, max_iter=100):
    """
    Método da Secante para encontrar raízes de f(x).
    Não requer a derivada analítica, apenas dois pontos iniciais x0 e x1.
    """
    for n in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        
        if f1 - f0 == 0:
            print("Erro: Divisão por zero no cálculo da secante.")
            return None
            
        x_novo = x1 - f1 * ((x1 - x0) / (f1 - f0))
        
        if abs(x_novo - x1) <= epsilon or abs(f(x_novo)) <= epsilon:
            print(f"[Secante] Convergiu em {n} iterações. Raiz: {x_novo:.8f}")
            return x_novo
            
        x0, x1 = x1, x_novo
        
    print("[Secante] Máximo de iterações atingido. Não convergiu.")
    return None


def gradiente_descendente(f_grad, x0, learning_rate=0.01, epsilon=1e-6, max_iter=1000):
    """
    Método do Gradiente Descendente para otimização (encontrar mínimos).
    Requer a função do gradiente e um escalar para a taxa de aprendizado.
    """
    x = np.array(x0, dtype=float)
    
    for n in range(1, max_iter + 1):
        grad = np.array(f_grad(x))
        
        x_novo = x - learning_rate * grad
        
        if np.linalg.norm(grad) <= epsilon:
            print(f"[Gradiente] Convergiu em {n} iterações. Mínimo em: {x_novo}")
            return x_novo
            
        x = x_novo
        
    print("[Gradiente] Máximo de iterações atingido. Minimizo aproximado em:", x)
    return x

