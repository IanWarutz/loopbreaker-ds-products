# 📊 Mood Identifier – Usage Example

from mood_tracker import MoodTracker

# 1️⃣ Create a MoodTracker for 7 days
tracker = MoodTracker(days=7)

# 2️⃣ Log your mood for each day (choose from the suggested moods or customize)
tracker.log_mood("Happy")
tracker.log_mood("Neutral")
tracker.log_mood("Excited")
tracker.log_mood("Sad")
tracker.log_mood("Motivated")
tracker.log_mood("Tired")
tracker.log_mood("Happy")

# 3️⃣ Get a summary of your mood week
summary = tracker.get_summary()

# 4️⃣ Print the results
print("📝 Your Mood Week Summary:")
print(f"🌟 Average Mood: {summary['average_mood']}")
print(f"👍 Best Day(s): {summary['best_days']} ({summary['best_mood']})")
print(f"👎 Worst Day(s): {summary['worst_days']} ({summary['worst_mood']})")
print(f"🔁 Most Frequent Mood: {summary['most_frequent_mood']}")