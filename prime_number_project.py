def isprime(n):
    is_prime=True
    i=2
    while is_prime:        
        if n/i==round(n/i) and i<n:
            
            is_prime=False
        elif i==n-1:
            break
        else:
            i+=1
    if is_prime:
        return f"{n} is a Prime Number"
    else:
        return f"{n} is not a Prime Number"


print(isprime(351))
print(isprime(326))
print(isprime(303))
print(isprime(313))


for i in range(100,152):
    print(isprime(i))
