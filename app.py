import json

class Flashcards:
    def __init__(mode, cards, answer):
        mode.cards = cards
        mode.answer = answer
    def points(cards, answer):
        json.dump(self.cards, file, indent=4)
def load_from_file(cls, filename="Flashcards.json"):
        try:
            with open(filename, "r") as f:
                cards = json.load(f)
            return cls(cards)
        except FileNotFoundError:
            return cls()  

flashcards = Flashcards.load_from_file()

flashcards.add_flashcard("x")
flashcards.add_flashcard("ye")


flashcards.save_to_file()

card_data = [card.to_dict() for card in cards]

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
    flashcards = Flashcards.load_from_file()

correct_answer = ()
word = input("Enter answer")
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


Flashcards[word] = answer
correct_answer = 0
total_questions = 0
streak = 0



if answer.strip().lower() == answer_strip.lower:


    with open("card.json", "w") as file:
      json.dump(card_data, file, indent=4)

    flashcards.save_to_file()


start_quiz()


