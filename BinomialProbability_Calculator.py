
#This Python script calculates the probability for n choose k in a binomial probability distribution.
#Functions are described in the docstrings.
#!/usr/bin/env python3

print('-------------------')
print("This will calculate the probability for n choose k in a binomial probability distribution.")
p = float(input('Choose the probability for success (1 success for 1 trial, on  a 0 to 1 scale): '))
k = float(input('Choose the number of successes: '))
n = int(input('Choose the number of trials: '))
print("---")
print("This creates '{} choose {}' with p of {}.".format(n,k,p))
print("I will now return the combined probability using the 'n choose k' binomial coefficient formula (n!/((n-k)!*k!)) together with the base probability (p**k * (1-p)**(n-k)):")

def __factorial__(n):
    """
    The factorial function takes input n and return the factorial.

    Takes n (int) as input and returns the factorial of n. This function is built in using a for loop to circumvent requiring the math library

    Examples:
    __factorial__(3) returns 6, because 3*2*1 is 6
    __factorial__(5) returns 120, because 5*4*3*2*1 is 120
    """
    fact = 1
    for i in range(1, int(n)+1):
        fact *= i
    return fact
fact = __factorial__(n)

def __calculate_prob__(p,k,n):
    prob_total = p**k * (1-p)**(n-k)
    return prob_total
print("base probablity: ", __calculate_prob__(p,k,n))
prob_total = __calculate_prob__(p,k,n)


# using math library for factorial instead:

#def __calculate_binom_coeff__(n,k):
#   binom_coeff = math.factorial(n) / ( math.factorial((n-k)) * math.factorial(k) )
#   return binom_coeff
#print("binomial coefficent: ", __calculate_binom_coeff__(n,k))
#binom_coeff = __calculate_binom_coeff__(n,k)


def __calculate_binom_coeff__(n,k):
    binom_coeff = fact / (__factorial__((n-k)) * __factorial__(k) )
    return binom_coeff
print("binomial coefficent: ", __calculate_binom_coeff__(n,k))
binom_coeff = __calculate_binom_coeff__(n,k)



def calculate_answer(prob_total, binom_coeff):
    """
    The calculate_answer() function takes the two inputs prob_total and binom_coeff

    1) The prob_total input takes the returned value from the __calculate_prob__(p,k,n)function. This is the
    probability calculated as p**k * (1-p)**(n-k)

    2) The binom_coeff input takes the returned value from the __binom_coeff__(n,k)function. This uses a combinatrics formula to
    calculate the binomial coefficient (n Choose k). The formula is n!/(k!(n-k)!).

    Multiplying these two inputs together results in the binomial probability.
    """
    answer = prob_total * binom_coeff
    return answer
answer = calculate_answer(prob_total, binom_coeff)
answer2 = calculate_answer(prob_total, binom_coeff) * 100
print("The probability is: {:.2f} (or {:.0f}%)".format(answer, answer2))
print("-----------")
