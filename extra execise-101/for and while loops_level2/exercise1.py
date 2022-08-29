# 📌 Description:
#
#         Write a Python program that checks if a number is prime or not.
#
#         If the number is prime, it should print "Prime".
#
#         If the number is not prime, it should print "Not prime".
#
# A prime number is only divisible by 1 and by itself. It is not the product of two smaller natural numbers

def check_prime(n):
    i=2
    for i in range(2 , n):
        if float(n % i) == 0:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
check_prime(8)




