def min_max_scaling(arr):
    min_val = min(arr)
    max_val = max(arr)
    scaled_arr = [(x - min_val) / (max_val - min_val) for x in arr]
    return scaled_arr


def can_charge(charger, laptop, tolerance):
    return charger >= laptop and charger <= laptop + tolerance


def calculate_score(hackathons_won, codeforces_rank, research_articles):
    weighted_score = (
        0.5 * hackathons_won + 0.3 * codeforces_rank + 0.2 * research_articles
    )
    return weighted_score


# Parse input
t = int(input())
for _ in range(t):
    C, L, S = map(int, input().split())
    chargers = list(map(int, input().split()))
    laptops = list(map(int, input().split()))
    tolerances = list(map(int, input().split()))
    hackathons_won = list(map(int, input().split()))
    codeforces_rank = list(map(int, input().split()))
    research_articles = list(map(int, input().split()))

    # Determine which chargers can charge each laptop
    chargers_for_laptop = []
    for laptop_power, tolerance in zip(laptops, tolerances):
        chargers_for_this_laptop = [
            charger
            for charger in chargers
            if can_charge(charger, laptop_power, tolerance)
        ]
        chargers_for_laptop.append(chargers_for_this_laptop)

    # Calculate score for each student
    scores = []
    for i in range(S):
        score = calculate_score(
            hackathons_won[i], codeforces_rank[i], research_articles[i]
        )
        scores.append(score)

    # Select students with highest scores and check if their laptops can be charged
    total_hackathons_won = 0
    selected_students = []
    # Select students with highest scores and check if their laptops can be charged
    total_hackathons_won = 0
    selected_students = []
    for i in sorted(range(len(scores)), key=lambda k: scores[k], reverse=True):
        if len(chargers_for_laptop) == 0:
            break
        if len(chargers_for_laptop[0]) > 0:
            total_hackathons_won += hackathons_won[i]
            selected_students.append(i)
            chargers_for_laptop.pop(0)

    # Output total number of hackathons won by the selected team
    if len(selected_students) == 0:
        print("-1")
    else:
        print(total_hackathons_won)
