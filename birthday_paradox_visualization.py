import numpy as np
import matplotlib.pyplot as plt

def birthday_paradox_simulation(num_simulations, num_people):
    # initialize match count
    match_count = 0

    # run simulations
    for _ in range(num_simulations):
        # generate random birthdays
        birthdays = np.random.randint(1, 366, size=num_people)
        unique_birthdays = np.unique(birthdays)

        # check for matches
        if len(birthdays) != len(unique_birthdays):
            match_count += 1

    # calculate probability of matching birthdays
    probability = match_count / num_simulations
    return probability

def visualize_birthday_paradox(num_people_list, num_simulations=10000):
    probabilities = []

    # run simulations for different group sizes
    for num_people in num_people_list:
        probability = birthday_paradox_simulation(num_simulations, num_people)
        probabilities.append(probability)

    # plot the results
    plt.plot(num_people_list, probabilities, marker='o')
    plt.title('Birthday Paradox Simulation')
    plt.xlabel('Number of People')
    plt.ylabel('Probability of Matching Birthdays')
    plt.grid(True)
    plt.show()

# list of group sizes for simulations (1 to 100)
num_people_list = list(range(1, 101))
visualize_birthday_paradox(num_people_list)