''' All Prime numbers in a list of integer from 1 to n'''
def SieveOfEratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    # If num is divisible by a factor greater than it's square root
    # then it means that the other factor is less than it's square root
    for num in range (2, int(n**0.5)+1):        
        if is_prime[num]:               # Avoid redondants multiples checking
            # We can start at num*num for the same reason why we too n**0.5
            for multiple in range(num*num, n+1, num):   
                is_prime[multiple] = False
    prime_numbers = [num for num in range(2, n+1) if is_prime[num]]
    return prime_numbers

''' Return the first N prime numbers in a list'''
def findFirstNPrimeNumbers(N):
    ''' 
    Each number greater than 5 can be written in the form :
    -> 6k, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5. 
    Of which, only 6k+1 and 6k+5 could be not divisible
    by either 2 or 3. So we need to check for this numbers only
    -> 6k+5 : num % i == 0 | 6k+1 : num % (i+2) == 0
    '''
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i*i <= num:
            if num % i == 0 or num % (i+2) == 0:
                return False
            i += 6
        return True
    
    prime_numbers = []
    num = 2
    while len(prime_numbers) < N:
        if is_prime(num):
            prime_numbers.append(num)
        num += 1
    return prime_numbers

''' Return all primes numbers in a sorted list of non continuous integer'''
def findPrimeNumbersInList(num_list):
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i*i <= num:
                if num % i == 0 or num % (i+2) == 0:
                    return False
                i += 6
            return True
        prime_numbers = []
        for num in num_list:
            if is_prime(num):
                prime_numbers.append(num)
        return prime_numbers

    #

# If some numbers are repeated multiple times, especially if large number,
# using memoization can increase efficiency