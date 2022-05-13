import random
import math

def pAdicNormInverse(prime, num):
    if num < 0:
        raise ValueError("input was less than zero")
    
    if num == 0:
        return 0
    
    norm = 1
    while num % prime == 0:
        num /= prime
        norm *= prime
    return norm

def chooseFromDistribution(arr, dist, num):
    total = 0
    for d in dist:
        total += d
    
    output = []
    for i in range(num):
        r = total * random.random()
        s = 0
        for j in range(len(dist)):
            s += dist[j]
            if s > r:
                output.append(arr[j])
                break
    
    output.sort()
    return output

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
DIST = [1/p for p in PRIMES]

ITERATIONS = 10000
numGuesses = [0] * 11
for i in range(ITERATIONS):
    options = list(range(1, 1001))
    target = random.randint(1, 1000)
    primes = chooseFromDistribution(PRIMES, DIST, 10)
    #print(f"Primes are {primes}")

    for guesses in range(10):
        guess = random.choice(options)
        norm = pAdicNormInverse(primes[guesses], abs(target - guess))
        if norm == 0:
            # Guess was correct
            #print(f"Guess {guess} was Correct!")
            numGuesses[guesses] += 1
            break
        if guesses == 9:
            # Wrong on the tenth guess
            # No need to refine options
            #print(f"Guess: {guess} Norm: 1/{norm}")
            #print(f"Failed! Target was {target}")
            numGuesses[10] += 1
            break
        
        #print(f"Guess: {guess} Norm: 1/{norm}")
        for j in range(len(options)-1, -1, -1):
           if pAdicNormInverse(primes[guesses], abs(options[j] - guess)) != norm:
               options.pop(j)


totalWins = 0
weightedSum = 0
for i in range(10):
    totalWins += numGuesses[i]
    weightedSum += numGuesses[i] * (i + 1)
    print(f"{i+1}: {numGuesses[i] * 100 / ITERATIONS:.4}%")
print(f"Fail: {numGuesses[10] * 100 / ITERATIONS:.4}%")
print(f"Average (among wins): {weightedSum / totalWins:.3}")
print(f"Win Percentage: {totalWins * 100 / ITERATIONS:.3}%")