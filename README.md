# Desafio Codeforces — Mentoria Codificadas | Além do Código

## Sobre este repositório

Este repositório contém minha resolução para o desafio final de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.

---

## Problemas escolhidos

| Nome do problema | LInk | Dificuladade |
| --------- | ------- | ------------- |
| Melância | [Ver no Codeforces](https://codeforces.com/problemset/problem/4/A) | 800 |

---

## Problema 1 — [Melância]

### O que o problema pede?

 Encontrar uma maneira de dividir o peso da melância entre dois amigos e informar se a divisão resulta em números pares.

---

### Como eu resolvi?

Usando a função MOD2 (%) para identificar se o peso da melância é um número par e maior que zero.

---

### Código

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

## IA utilizada

**Qual IA você usou?**
Usei o Copilot na edição do código na IDE Vscode para entender e ajustar erros no README.md e Gemini para identificar o erro de processamento na plataforma Codeforces.

**Como a IA te ajudou?**

O Copilot me ajudou a recordar como usar o run para testar o código e Gemini me ajudou a remover a interação textual com o usuário para que a entrada fosse numérica e a saída YES ou NO. Tornou meu código mais limpo com boas práticas.

---

## Reflexão

### Dificuldades encontradas

O que foi mais difícil foi entender o problema e realizar a operação de forma que a saída fosse correspondente ao teste.

---

### O que aprendi

Aprendi que mesmo que a lógica do meu código esteja correta e funcional no VSCode, pode não ser aceito na plataforma do Codeforces. A forma como são feitos os testes impõe a necessidade de correspondencia no input e output.

---

### Como foi a experiência?

Foi bom realizar os comando do git para clonar, editar, adicionar, commitar e fazer o pull request para o repositório remoto. Tive um problema de choque do commit porque fiz alterações tanto no repositório local quanto no remoto. Isso me ajudou a entender o processo do merge para resolução do conflito. Aprendi
