l = []
for i in range(20):
    n = int(input())
    l.append(n)
print("Numbers divisible by 5:")
for n in l:
    if n % 5 == 0:
        print(n)
