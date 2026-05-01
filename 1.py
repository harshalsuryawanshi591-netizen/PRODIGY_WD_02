S = [0,1,2]

print("* |" , end ="")

for b in S:
    print(b, end = " ")

print("\n-----" + "-------")

for a in S:
    print(a, end = "|")
    for b in S:
        result = (a + b) % 3
        print(result, end = " ")
    print()
