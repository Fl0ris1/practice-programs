#Find All Prime Numbers From 1 - 100
def primeCheck(num):
    for i in range(2, num):
        if num % i == 0:
            return 0

for i in range(2, 100): #0 And 1 Are NOT Prime Numbers
    if primeCheck(i) == None:
        print(i, end = " ")