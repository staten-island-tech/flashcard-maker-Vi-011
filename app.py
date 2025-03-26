word = input("Enter answer")

answer = input(f"Answer for '{word}': ").strip()
Flashcards[word] = answer
correct_answer = 0
total_questions = 0
streak = 0

Flashcards = [
    card(),
    card(),
    card()
]

card_data = [card.to_dict() for card in cards]

with open("card.json", "w") as file:
    json.dump(card_data, file, indent=4)

class Flashcards:
    def __init__(mode, cards, answer):
        mode.cards = cards
        mode.answer = answer
    def points(cards, answer):
    to_dict(mode):
    return {"make": mode.cards, mode.answer,}
   
