print("📘 Welcome to Mariam's Smart Math Quiz Bot 🤖")

score = 0

questions = [
    ("What is 5 + 3? ", 8),
    ("What is 10 - 4? ", 6),
    ("What is 3 x 3? ", 9),
    ("What is 12 / 4? ", 3),
    ("What is 2 ** 3? ", 8),
    ("What is 5*2? ", 10)
]

for i, correct_answer in questions:
    ans = int(input(i))
    if ans == correct_answer:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

# Final Result
print("\n🏁 Quiz Finished!")
print("🧮 Your score:", score, "out of", len(questions))

# Emoji Reaction
if score == len(questions):
    print("🎉 Amazing! You're a math genius!")
elif score >= 3:
    print("👍 Good job! Keep practicing!")
else:
    print("😅 Don't worry! Try again tomorrow.")
