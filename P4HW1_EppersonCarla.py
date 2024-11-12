# Carla Epperson
# 11/12/2024
# P4HW1_EppersonCarla
# This program asks the user for a set number of scores, validating each to ensure it's between 0 and 100.

""" Pseudocode:

1.Ask how many scores the user wants to enter and save that number as num_scores.
2.Create an empty list called scores to store the valid ones.
3.Loop from 1 to num_scores: a. Keep asking for a score until it’s between 0 and 100.
4.If the score is valid, add it to scores and move to the next.
5.If it’s not, let the user know and ask again.
6.When all scores are entered, print out the list of valid scores.

"""



num_scores = int(input("How many scores do you want to enter?: "))
scores = []

for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i + 1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!! Please enter a score between 0 and 100.")

print("\nScores entered:", scores)
