lastNum=0
currentNum=1
temp=0


print(lastNum, end = " ")
print(currentNum, end = " ")
for i in range(10):
    temp = currentNum
    currentNum += lastNum
    print(currentNum, end = " ")
    lastNum = temp