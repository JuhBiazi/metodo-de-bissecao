import math

def f(x):
    return math.exp(x) - x - 2
# Variaveis
a = -2
b = 0
E = 10 ** -3

# Verificação para ver se a função atravessa o eixo x
def bissecao(f, a, b, E):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")
    
    iteracoes = 0
    while (b - a) / 2 > E:
        X = (a + b) / 2
        if f(X) == 0:
            break
        elif f(X) * f(a) < 0:
            b = X
        else:
            a = X
        iteracoes += 1

    raiz = (a + b) / 2
    return raiz, iteracoes


raiz, iteracoes = bissecao(f, a, b, E)
print(f"Raiz encontrada: {raiz:.7f}")
print(f"Iterações necessárias: {iteracoes}")