import random
from math import prod

def theoretical_birthday_probability(num_people):
    # calculate the theoretical birthday paradox probability
    probability = 1 - prod([(365 - i) / 365 for i in range(num_people)])
    return probability

def birthday_paradox_probability(num_people, num_simulations=10000):
    # initialize the count of cases
    same_birthday_count = 0

    # simulate the birthday paradox
    for _ in range(num_simulations):
        # randomly select the birthday for each person
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        
        # check duplicated birthdays
        if len(birthdays) != len(set(birthdays)):
            same_birthday_count += 1

    # calculate the probability
    probability = same_birthday_count / num_simulations
    return probability

# get the number of people
num_people = int(input("Enter the number of people: "))

# calculate the actual birthday paradox probability 
result_probability = birthday_paradox_probability(num_people)

# calculate the theoretical birthday paradox probability
theoretical_probability = theoretical_birthday_probability(num_people)

# print the results
print(f"actual birthday paradox probability: {result_probability:.2%}")
print(f"theoretical birthday paradox probability: {theoretical_probability:.2%}")
