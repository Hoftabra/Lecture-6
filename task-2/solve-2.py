
n = int(input())
x = 0

for _ in range(n):
    q = int(input())
    if q % 6 == 0 and q % 10 == 4:
        x += q

print(x)
