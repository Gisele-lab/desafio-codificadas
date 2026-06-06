import sys

def solve():
    # sys.stdin.read().split() lê toda a entrada de uma vez e separa por espaços/quebras de linha
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento da entrada é o número de casos de teste (t)
    t = int(input_data[0])
    
    # Índice para rastrear nossa posição na leitura de input_data
    idx = 1
    
    # LOOP PRINCIPAL: Roda uma vez para cada caso de teste
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        resultado = []
        esquerda = 1
        direita = 2 * n
        
        # LOOP DE CONSTRUÇÃO: Roda 'n' vezes para construir o array de tamanho n
        for i in range(n):
            # Se 'i' for par (0, 2, 4...), pegamos o número do final (maior)
            if i % 2 == 0:
                resultado.append(direita)
                direita -= 1  # Decrementa o ponteiro da direita
            # Se 'i' for ímpar (1, 3, 5...), pegamos o número do começo (menor)
            else:
                resultado.append(esquerda)
                esquerda += 1  # Incrementa o ponteiro da esquerda
        
        # Converte a lista de inteiros em string separada por espaços e imprime
        print(*(resultado))

if __name__ == '__main__':
    solve()