import json
import os
import datetime
import random

# Mood options
mood_options = ["😄 Happy", "😔 Sad", "😰 Anxious", "😐 Neutral", "😴 Tired", "🤩 Excited", "🧘 Calm"]

# Affirmations and reinforcements
positive_reinforcements = [
    "Keep the positive vibes going!",
    "Fantastic! Celebrate your good days.",
    "You’re doing great—keep enjoying the little things.",
    "Your positive energy is inspiring!"
]

negative_affirmations = [
    "It's okay to have tough days—be gentle with yourself.",
    "Remember, feelings are temporary and you are resilient.",
    "You deserve kindness and care, especially on hard days.",
    "Taking a moment for self-care can make a difference."
]

call_to_action = (
    "\nWe noticed you've had several low mood days. "
    "Consider reaching out to someone you trust, practicing self-care, "
    "or talking to a mental health professional. You’re not alone!"
)

USER_LOG_FILE = "mood_user_logs.json"

def load_user_logs():
    if os.path.exists(USER_LOG_FILE):
        with open(USER_LOG_FILE, "r") as f:
            return json.load(f)
    else:
        return {"logs": [], "last_entry": None, "streak": 0}

def save_user_logs(data):
    with open(USER_LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_streak(user_data, today):
    last_entry = user_data.get("last_entry")
    if last_entry:
        last_date = datetime.datetime.strptime(last_entry, "%Y-%m-%d").date()
        if (today - last_date).days == 1:
            user_data["streak"] += 1
        elif (today - last_date).days > 1:
            user_data["streak"] = 1
    else:
        user_data["streak"] = 1
    user_data["last_entry"] = today.isoformat()
    return user_data

def get_moods():
    moods = []
    print("🌈 Mood Tracker – Reflect on Your Last 7 Days 🌈")
    for i in range(7):
        print(f"\nDay {i+1} mood options:")
        for idx, mood in enumerate(mood_options, 1):
            print(f"{idx}. {mood}")
        while True:
            try:
                choice = int(input("Select your mood (1–7): "))
                if 1 <= choice <= 7:
                    moods.append(mood_options[choice - 1])
                    break
                else:
                    print("Invalid. Select again (1–7): ")
            except ValueError:
                print("Please enter a number between 1 and 7.")
    return moods

def analyze_moods(moods):
    print("\n📝 Your Mood Log for the Week:")
    negative_count = 0
    for i, mood in enumerate(moods, 1):
        print(f"Day {i}: {mood}", end=' ')
        if mood in ["😔 Sad", "😰 Anxious", "😴 Tired"]:
            print(f"\n   💬 {random.choice(negative_affirmations)}")
            negative_count += 1
        elif mood in ["😄 Happy", "🤩 Excited", "🧘 Calm"]:
            print(f"\n   🌟 {random.choice(positive_reinforcements)}")
        else:
            print()
    if negative_count >= 4:
        print(call_to_action)
    else:
        print("\n🎉 Great job tracking your moods! Come back tomorrow for another check-in and keep building awareness.")
    print("\nTip: Consistent mood tracking helps you notice patterns and take positive steps. Set a daily reminder to log your mood!")

def main():
    today = datetime.date.today()
    user_data = load_user_logs()
    user_data = update_streak(user_data, today)
    
    print(f"\n🔥 Your current mood tracking streak: {user_data['streak']} day(s) in a row! Keep it up!")

    moods = get_moods()
    analyze_moods(moods)

    # Store logs
    log_entry = {
        "date": today.isoformat(),
        "moods": moods
    }
    user_data["logs"].append(log_entry)
    save_user_logs(user_data)

    print("\n🗂️ Your moods have been saved. Check back tomorrow to continue your streak!")

if __name__ == "__main__":
    main()