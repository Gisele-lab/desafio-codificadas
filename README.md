# Desafio Codeforces — Mentoria Codificadas | Além do Código

## Sobre este repositório

Este repositório contém minha resolução para o desafio final de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.

---

## Problemas escolhidos

| # | Nome do problema | Link | Dificuldade |
|---|------------------|------|-------------|
| 1 | Melancia         | [Ver no Codeforces](https://codeforces.com/problemset/problem/4/A) | 800              |

---

## Problema 1 — [Watermelon]

### O que o problema pede?
<!-- Desafio de dois amigos que querem dividir a melância em duas partes de modo que o peso deve ser número par diferente de zero. -->

### Como eu resolvi?
<!-- Primeiro, defini uma função para receber o peso da melância. Em seguida, apliquei o método de dividir por 2. Se o resultado for igual a zero, o peso é par, então imprime YES. Senão, o peso é impar e imprime NO. Ao final a função se autoinvoca. -->

### Código

```Python
# def solve():
    # Remova a frase de dentro do input()
    peso_melancia = int(input())
    
    if peso_melancia % 2 == 0 and peso_melancia > 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
```

## IA utilizada

**Qual IA você usou?**
<!-- Usei Github Copilot na IDE do VsCode para identificar erros no código e escrever de forma simples com boas práticas de programação. Ao enviar meu código na Codeforces, o mesmo não foi aceito. Gemini me explicou onde estava o erro-->

**Como a IA te ajudou?**
<!-- Descreva como você usou a IA no processo. Ela explicou o problema? Sugeriu uma estratégia? Ajudou a corrigir um erro? -->

---

## Reflexão

### Dificuldades encontradas
<!-- O que foi mais difícil? Entender o problema? Escrever o código? Usar o GitHub? -->

### O que aprendi
<!-- O que você aprendeu de novo com este desafio? Pode ser sobre programação, sobre usar IA, ou qualquer coisa. -->

### Como foi a experiência?
<!-- Conta um pouco como foi no geral. O que mais gostou? O que mudaria? -->
README.md
Exibindo README.md…
