num=[]
factorial=[]

for i in range(5):
    inp=int(input("Input A Number: "))
    num.append(inp)

print(f"Original List: {num}")
    
for i in range(len(num)):
    for j in range(1,num[i]):
        num[i] *= j
        
    factorial.append(num[i])
    
print(f"Factorials: {factorial}")