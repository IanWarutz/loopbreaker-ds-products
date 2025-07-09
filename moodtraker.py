# Mood options
mood_options = ["😄 Happy", "😔 Sad", "😰 Anxious", "😐 Neutral", "😴 Tired", "🤩 Excited", "🧘 Calm"]

def get_moods():
    moods = []
    print("Rate your mood for the last 7 days:")
    for i in range(7):
        print(f"\nDay {i+1} mood options:")
        for idx, mood in enumerate(mood_options, 1):
            print(f"{idx}. {mood}")
        choice = int(input("Select your mood (1–7): "))
        while choice < 1 or choice > 7:
            choice = int(input("Invalid. Select again (1–7): "))
        moods.append(mood_options[choice - 1])
    return moods

def analyze_moods(moods):
    print("\nYour Mood Log for the Week:")
    for i, mood in enumerate(moods, 1):
        print(f"Day {i}: {mood}")

# Main App
moods = get_moods()
analyze_moods(moods)
