import numpy as np
import matplotlib.pyplot as plt

def birthday_paradox_simulation(num_simulations, num_people):
    match_count = 0

    for _ in range(num_simulations):
        birthdays = np.random.randint(1, 366, size=num_people)
        unique_birthdays = np.unique(birthdays)
        
        if len(birthdays) != len(unique_birthdays):
            match_count += 1

    probability = match_count / num_simulations
    return probability

def visualize_birthday_paradox(num_people_list, num_simulations=10000):
    probabilities = []

    for num_people in num_people_list:
        probability = birthday_paradox_simulation(num_simulations, num_people)
        probabilities.append(probability)

    plt.plot(num_people_list, probabilities, marker='o')
    plt.title('Birthday Paradox Simulation')
    plt.xlabel('Number of People')
    plt.ylabel('Probability of Matching Birthdays')
    plt.grid(True)
    plt.show()

# 시뮬레이션을 위한 인원 수 리스트 (1부터 100까지)
num_people_list = list(range(1, 101))
visualize_birthday_paradox(num_people_list)
