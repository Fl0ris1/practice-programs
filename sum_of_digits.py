n=int(input("Enter A Number: "))
num=n
sum=0

"""
1234
digit=0
digit=4
sum=4
num=remaining digits
repeat


"""
while num>0:
    digit=num%10
    sum+=digit
    num=num//10

print(f"The Sum Of Your Number Is: {sum}")