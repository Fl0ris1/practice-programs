nums1=[]
nums2=[]
sums=[]

for i in range(0,5):
    inp=int(input("Input The First 5 Numbers: "))
    nums1.append(inp)
    
for i in range(0,5):
    inp=int(input("Input The Second 5 Numbers: "))
    nums2.append(inp)
    
for i in range(len(nums1)):
    sums.append(nums1[i]+nums2[i])
    
print(f"First 5 Numbers: {nums1}")
print(f"Second 5 Numbers: {nums2}")
print(f"Sum Of The 5 Numbers: {sums}")