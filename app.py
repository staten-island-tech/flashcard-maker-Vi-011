import json

class Flashcards:
    def __init__(self, cards=None):
        self.cards = cards if cards else {}

    def add_flashcard(self, word, answer):
        self.cards[word] = answer

    def save_to_file(self, filename="Flashcards.json"):
        with open(filename, "w") as file:
            json.dump(self.cards, file, indent=4)

    @classmethod
    def load_from_file(cls, filename="Flashcards.json"):
        try:
            with open(filename, "r") as f:
                cards = json.load(f)
            return cls(cards)
        except FileNotFoundError:
            return cls()

flashcards = Flashcards.load_from_file()

def start_quiz():
    correct_answers = 0
    streak = 0
    streak_bonus = 0

    while True:
        word = input("Enter word (or 'exit' to quit): ").strip()
        if word == "exit":
            break

        if word in flashcards.cards:
            answer = input(f"Answer for '{word}': ").strip()
            
            if flashcards.cards[word].lower() == answer.lower():
                print("Correct!")
                correct_answers += 1
                streak += 1

                
                if streak > 3:
                    streak_bonus += 1
                    print("Streak bonus awarded!")
            else:
                print("Incorrect.")
                streak = 0  
        else:
            print(f"Word '{word}' not found in flashcards.")

    print(f"Total correct answers: {correct_answers}")
    print(f"Streak bonus: {streak_bonus}")

# Start quiz
start_quiz()

# Save the flashcards to file at the end
flashcards.save_to_file()