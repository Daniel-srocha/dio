n = int(input())

for i in range(n):
    x, y = input().split(" ")
    print ("nao " if len(y) > len(x) or x[len(x) - len(y): len(x)] != y else "","encaixa")