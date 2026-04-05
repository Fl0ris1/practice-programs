odd=[]
even=[]
nums=[]
for i in range(10):
    inp=int(input("Input A Number: "))
    nums.append(inp)
    
for i in range(len(nums)):
    if nums[i]%2!=0:
        odd.append(nums[i])
    else:
        even.append(nums[i])
        
print(f"Original List: {nums}")
print(f"Even Numbers: {even}")
print(f"Odd Numbers: {odd}")