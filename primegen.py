primenth = [0]

def get_prime_nth(n):
    while n>=len(primenth):
        print("generating more")
        mx_now*=10
        SieveOfEratosthenes(mx_now)
    return primenth[n]
mx_now = 0

def SieveOfEratosthenes(num):
    global mx_now
    mx_now = num
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

  
    for p in range(2, num+1):
        if prime[p]:
            primenth.append(p)
