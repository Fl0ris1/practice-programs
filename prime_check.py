num=int(input())
div= []

#print(7%3) gives 1
for i in range(1, 10):
    remainder = num % i
    if remainder == 0:
        div.append(i)

if len(div)<=2:
    print("This Is A Prime Number")
else:
    print("This Is NOT A Prime Number")