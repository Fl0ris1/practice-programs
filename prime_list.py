nums=[]
primes=[]
c=0

for i in range(10):
    inp=int(input("Input A Number: "))
    nums.append(inp)
    
for i in range(len(nums)):
    c=0
    for j in range(2,nums[i]):
        if nums[i] % j == 0:
            c=1
            break
        
    if c == 0:
        primes.append(nums[i]) 

print(f"Original Numbers: {nums}")
print(f"Prime Numbers: {primes}")