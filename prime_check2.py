num = int(input("Input A Number"))
p = 0

for i in range(2, num):
    if num%i == 0:
        p = 1
        break

if p == 1:
    print(f"{num} Is Not A Prime Number")
else:
    print(f"{num} Is A Prime Number")