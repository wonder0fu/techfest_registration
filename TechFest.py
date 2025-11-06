# TechFest Registration System A Python program that records event participants and analyzes track diversity.
#   Antonio Andres R. Dinglasan - Midterm - BTCS1

# Task 1 Registration Setup
print ('\nWelcome To SMIT TechFest!!')
print ('\nEvent organized by Antonio Dinglasan of APPDAET BTCS1')

num_participants = int(input('How many participants will register? '))
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
for i, j in enumerate(participants, 1):
    print(f"{i}. {j['name']} - {j['track']}")

# Task 3: Track Diversity Report
unique_tracks = {p["track"] for p in participants}

if len(unique_tracks) < 2:
    print("\nNot enough variety in tracks.")
else:
    print("\nTracks offered in this event:", ", ".join(unique_tracks))

# Task 4 Duplicate Name Detection

duplicate_name = set ()
duplicate_found = False

for j in participants:
    if j["name"] in duplicate_name:
        print(f"Duplicate Name Found: {j['name']}")
        duplicate_found = True
        break
    duplicate_name.add(j["name"])

if not duplicate_found:
    print ("No Duplicate Names Found")

#Task 5: Track Summary Report
track_summary = {}
for i in participants:
    track = i["track"]
    if track in track_summary:
        track_summary[track] += 1
    else:
        track_summary[track] = 1

print ("Participants per track:")
for track, count in track_summary.items():
    print(f"{track}: {count}")