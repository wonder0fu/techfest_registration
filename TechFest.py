# TechFest Registration System A Python program that records event participants and analyzes track diversity.


# Task 1 Registration Setup
print ('\nWelcome To SMIT TechFest!!')
print ('\nEvent organized by Antonio Dinglasan of APPDAET BTCS1')

num_participants = int(input('How many participants will register?'))
if num_participants <= 0:
    print('Invalid number of Participants')
    exit()

# Task 2 Collect Participant Information
participants = []
for i in range(num_participants):
    print(f"Enter Participant {i+1}: ")
    name = input("Enter Participant name: ")
    track = input("Enter chosen track: ")
    participants.append ({"name": name, "track": track})

print("Registered Participants:")
for i, p in enumerate(participants, 1):
    print(f"{i}. {p['name']} - {p['track']}")