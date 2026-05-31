def solve():
    peso_melancia = int(input())

    if peso_melancia % 2 == 0 and peso_melancia > 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__": 
    solve()