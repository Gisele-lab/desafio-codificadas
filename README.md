# Desafio Codeforces — Mentoria Codificadas | Além do Código

## Sobre este repositório

Este repositório contém minha resolução para o desafio final de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.

---

## Problemas escolhidos

| Nome do problema | LInk | Dificuldade |
| --------- | ------- | ------------- |
| Melância | [Ver no Codeforces](https://codeforces.com/problemset/problem/4/A) | 800 |
| Construindo um Array | [Ver no Codeforces](https://codeforces.com/problemset/problem/2231/A) | 800 |

---

## Problema 1 — [Melância]

### 1 O que o problema pede?

 Encontrar uma maneira de dividir o peso da melância entre dois amigos e informar se a divisão resulta em números pares.

---

### 1 Como eu resolvi?

Usando a função MOD2 (%) para identificar se o peso da melância é um número par e maior que zero.

---

### 1 Código

```def solve():
    peso_melancia = int(input())

    if peso_melancia % 2 == 0 and peso_melancia > 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__": 
    solve()
```

---

## Problema 2 — [Construindo um Array]

### 2 O que o problema pede?

O objetivo é construir uma lista (array) de tamanho $n$ contendo números inteiros $a_1, a_2, \dots, a_n$ que respeite duas condições básicas:
• Limite dos valores: Cada número escolhido deve estar entre $1$ e $2n$ ($1 \le a_i \le 2n$).
• Unicidade de elementos e somas: Se você juntar todos os números individualmente mais todas as somas de vizinhos adjacentes ($a_1+a_2$, $a_2+a_3$, etc.), nenhum valor pode se repetir. Todos precisam ser distintos.

---

### 2 Como eu resolvi?

Primeiro passo enteder o problema identificando padrão fixo que funcione com qualquer valor de $n$. Segundo, usar a função range() do Python onde, de forma rápida e fácil, criamos uma Progressão Aritimética de ímpares resultando em uma lista que atende as condições do problema.

---

### 2 Código

```import sys

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
```

---

## IA utilizada

**Qual IA você usou?**

Usei o Copilot na edição do código na IDE Vscode para entender e ajustar erros no README.md e Gemini para identificar o erro de processamento na plataforma Codeforces.

**Como a IA te ajudou?**

O Copilot me ajudou a recordar como usar o run para testar o código e Gemini me ajudou a remover a interação textual com o usuário para que a entrada fosse numérica e a saída YES ou NO. Tornou meu código mais limpo com boas práticas.  Para o segundo problema, achei a primeira solução confusa e difícil de entender. De modo que solicitei auxílio para construir de forma simples um array com as informações de primeiro elemento, último elemento e incremento.

---

## Reflexão

### Dificuldades encontradas

O que foi mais difícil foi entender o problema e realizar a operação de forma que a saída fosse correspondente ao teste. Para o segundo problema, recordar o que havia aprendido sobre a função range() na criação de array.

---

### O que aprendi

Aprendi que mesmo que a lógica do meu código esteja correta e funcional no VSCode, pode não ser aceito na plataforma do Codeforces. A forma como são feitos os testes impõe a necessidade de correspondencia no input e output. Também aprendi que nem sempre a solução da IA estará correta. Sempre questionar e testar.

---

### Como foi a experiência?

Foi bom realizar os comando do git para clonar, editar, adicionar, commitar e fazer o pull request para o repositório remoto. Tive um problema de choque do commit porque fiz alterações tanto no repositório local quanto no remoto. Isso me ajudou a entender o processo do merge para resolução do conflito. Aprendi outros comandos do git e como funcionam para o controle e versionamento do código.
