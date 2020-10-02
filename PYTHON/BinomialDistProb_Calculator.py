#import math  #needed for factorials, wil circumvent later with loop
print('-------------------')
print("This will calculate the probability for n choose k in a binomial probability distribution.")
p = float(input('Choose the probability for success (1 success for 1 trial, on  a 0 to 1 scale): '))
k = float(input('Choose the number of successes: '))
n = int(input('Choose the number of trials: '))
print("---")
print("This creates '{} choose {}' with p of {}.".format(n,k,p))
print("I will now return the combined probability using the 'n choose k' binomial coefficient formula (n!/((n-k)!*k!)) together with the base probability (p**k * (1-p)**(n-k)):")

def __factorial__(n):
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
    answer = prob_total * binom_coeff
    return answer
answer = calculate_answer(prob_total, binom_coeff)
answer2 = calculate_answer(prob_total, binom_coeff) * 100
print("The probability is: {:.2f} (or {:.0f}%)".format(answer, answer2))
print("-----------")