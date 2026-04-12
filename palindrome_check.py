inp=int(input("Input A Number\n"))
inp=str(inp)
str1=""
#1234321 if num[i]!=num[len(num)-i]  
for i in range(len(inp)-1,-1,-1):
    str1+=str(inp[i])

if str1==inp:
    print("Palindrome Number")

else: 
    print("Not A Palindrome")