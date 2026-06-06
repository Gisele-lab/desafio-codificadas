import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        # Definições baseadas nas regras do problema
        primeiro = 1
        ultimo = 2 * n - 1
        incremento = 2
        
        # Cria a lista de forma direta e sem loops manuais
        # Somamos o incremento ao 'ultimo' para o range incluir o valor final
        resultado = list(range(primeiro, ultimo + incremento, incremento))
        
        # Imprime o resultado desempacotado
        print(*(resultado))

if __name__ == '__main__':
    solve()