import json

class Flashcards:
    def __init__(self, cards=None):
        self.cards = cards if cards else {}
    
    def add_flashcard(self, word, answer):
        self.cards[word] = answer
    
    def to_dict(self):
        return self.cards

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


def start_quiz():
    flashcards = Flashcards.load_from_file()
    
    correct_answers = 0
    streak = 0
    streak_bonus = 0
    
    while True:
        word = input("Enter word: ").strip()
        if word == "exit":
            break

        answer = input(f"Answer for '{word}': ").strip()
        
        if word in flashcards.cards and flashcards.cards[word].lower() == answer.lower():
            print("Correct!")
            correct_answers += 1
            streak += 1
            if streak > 3:
                streak_bonus += 1
                print("Streak bonus awarded!")
        else:
            print("Incorrect.")
            streak = 0  

    print(f"Total correct answers: {correct_answers}")
    print(f"Streak bonus: {streak_bonus}")

    
    flashcards.save_to_file()


flashcards = Flashcards.load_from_file()

flashcards.add_flashcard("Python", "A programming language")
flashcards.add_flashcard("HTML", "A markup language")


flashcards.save_to_file()

start_quiz()