# TechFest Registration System A Python program that records event participants and analyzes track diversity.


# Task 1 Registration Setup
print ('\nWelcome To SMIT TechFest!!')
print ('\nEvent organized by Antonio Dinglasan of APPDAET BTCS1')

num_participants = int(input('How many participants will register?'))
if num_participants <= 0:
    print('Invalid number of Participants')
    exit()

# Task 2 Collect Participant Information