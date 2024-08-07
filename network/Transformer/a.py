import random
from collections import defaultdict

# List of people
people = ["Đạt", "Phong", "Thành", "Minh", "Hoàng", "Tài", "Nguyên", "Việt Anh", "Đức", "a.Duy", "Long", "Oppa", "c.Thảo", "Oanh", "Linh"]

# Function to create random pairs
def create_random_pairs(selected_people):
    random.shuffle(selected_people)
    pairs = []
    for i in range(0, len(selected_people), 2):
        if i+1 < len(selected_people):
            pairs.append((selected_people[i], selected_people[i+1]))
    return pairs

# Function to generate matches
def generate_matches(people, num_matches=30):
    matches = []
    match_count = defaultdict(int)
    temp_people = people.copy()

    while len(matches) < num_matches:
        if len(temp_people) < 6:
            temp_people = people.copy()

        selected_people = random.sample(temp_people, 6)
        for person in selected_people:
            temp_people.remove(person)
        
        pairs = create_random_pairs(selected_people)
        
        # Check if anyone is playing two times consecutively
        if matches and any(p in match for p in pairs for match in matches[-3:]):
            temp_people.extend(selected_people)
            continue

        # Add the pairs to the matches
        matches.extend(pairs)
        
        # Update the match count for each player
        for pair in pairs:
            match_count[pair[0]] += 1
            match_count[pair[1]] += 1

        # Check if the number of matches is reached
        if len(matches) >= num_matches:
            break
    
    return matches, match_count

# Generate the matches
matches, match_count = generate_matches(people)

# Print the results
print("Generated Matches:")
for match in matches:
    print(match)

print("\nMatch Count per Player:")
for player, count in match_count.items():
    print(f"{player}: {count} matches")
