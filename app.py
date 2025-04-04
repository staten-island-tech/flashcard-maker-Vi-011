
import json

class Flashcards:
    def __init__(self, cards=None):
        self.cards = cards if cards else {}
    def add_flashcard(self, word, answer):
        self.cards[word] = answer
    def save_to_file(self, filename="Flashcards.json"):
        with open(filename, "w") as file:
            json.dump(self.cards, file, indent=4)



card_data = [card.to_dict() for card in "cards"]

with open("card.json", "w") as file:
    json.dump(card_data, file, indent=4)

def load_from_file(cls, filename="Flashcards.json"):
    try:
        with open(filename, "r") as f:
                cards = json.load(f)
        return cls(cards)
    except FileNotFoundError:
            return cls()  

def start_quiz():

    while True:
       
        word = input("Enter answer")
        streak = 0
        streak_bonus = 0
        word = input("Enter word: ").strip()
        if word == "exit":
            break

        answer = input(f"Answer for '{word}': ").strip()
        
        if word in Flashcards.cards and Flashcards.cards[word].lower() == answer.lower():
            print("Correct!")
            correct_answers += 1
            streak += 1
            if streak > 3:
                streak_bonus += 1
                print("Streak bonus awarded!")
        else:
            print("Incorrect.")
            streak = 0  


with open("card.json", "w") as file:
      json.dump(card_data, file, indent=4)

print(f"Total correct answers: {correct_answers}")
print(f"Streak bonus: {streak_bonus}")

Flashcards.save_to_file()

start_quiz()


