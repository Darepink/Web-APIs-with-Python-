import requests, random

def get_trivia(category, name):
    url = f"https://opentdb.com/api.php?amount=1&category={category}&type=multiple"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["results"][0]

            question = data["question"]
            correct = data["correct_answer"]
            wrong = data["incorrect_answers"]
            choices = wrong + [correct]
            random.shuffle(choices)

            # Display question
            print(f"\n🎲 {name} Trivia Question:")
            print(question)
            for i, option in enumerate(choices, 1):
                print(f"{i}. {option}")

            # User answer input
            user_choice = input("\nEnter number: ")
            try:
                if choices[int(user_choice) - 1] == correct:
                    print("✅ Correct!\n")
                else:
                    print(f"❌ Wrong! The correct answer was: {correct}\n")
            except:
                print("⚠️ Invalid input.\n")
        else:
            print("❌ Couldn't fetch trivia.")
    except:
        print("⚠️ API error.")

# Trivia categories
categories = {
    "1": (9, "General Knowledge"),
    "2": (17, "Science & Nature"),
    "3": (15, "Entertainment: Video Games"),
}

while True:
    print("\nTrivia Menu\n1. General\n2. Science\n3. Games\n4. Exit")
    choice = input("Pick (1-4): ")

    if choice in categories:
        get_trivia(*categories[choice])
    elif choice == "4":
        print("🎉 Exiting.")
        break
    else:
        print("⚠️ Invalid choice.")
