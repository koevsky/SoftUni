n = int(input())
chem_set = set()
for _ in range(n):
    elements = input().split()
    for x in elements:
        chem_set.add(x)

print("\n".join(chem_set))