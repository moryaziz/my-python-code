def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def factorial2(n):
    pre=1
    current = 2
    fact = current * pre
    if n < 2 :
        return 1
    elif n == 2 :
        return 2
    else:
        for i in range(3,n+1):
            current = i
            pre = fact
            fact= current * pre
        return fact

def factorial3(n):
    pre=1
    current = 1
    fact = current * pre
    for i in range(1,n+1):
        current = i
        pre = fact
        fact= current * pre
        yield fact

print(factorial(50))
print(factorial2(50))
for num in factorial3(50):
    print(num)