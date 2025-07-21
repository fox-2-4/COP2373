import random


class Deck:

    def __init__(self, nof_decks):
        self.dealers_deck = [
            num + suit
            for suit in "\u2665\u2666\u2663\u2660"
            for num in "A23456789TJQK"
            for deck in range(nof_decks)
        ]
        self.current_hand = []
        self.discards = []
        random.shuffle(self.dealers_deck)

    def deal(self):
        if len(self.dealers_deck) < 1:
            random.shuffle(self.discards)
            self.dealers_deck = self.discards
            self.discards = []
            print("Reshuffling...")
        new_card = self.dealers_deck.pop()
        self.current_hand.append(new_card)

    def new_hand(self):
        self.discards += self.current_hand
        self.current_hand.clear()

    def display_current_hand(self):
        for i in range(len(self.current_hand)):
            print(f"({i + 1}) ", end="")
        print()
        for card in self.current_hand:
            print(f"{card}  ", end="")
        print("\n")

    def exchange_card(self, card_n):
        if card_n > len(self.current_hand) - 1 or card_n < 0:
            raise ValueError("Card number out of range")
        # 1. because we're working with the code from the book, this part is a little janky and relies on the fact that
        #    the deal() method doesn't care about the size of the current hand and deals a new card to the last position
        # 2. we add the card to swap to the discard pile without actually discarding it (yet) because it's effectively
        #    just there to hold the spot in the list for the future dealt card.
        self.discards += self.current_hand[card_n]              # add card to discards
        self.deal()                                             # deals to the end of the self.current_hand list
        self.current_hand[card_n] = self.current_hand.pop()     # move last dealt card to the specified position


def parse_int_list(x: str) -> list[int]:
    lines = x.split(",")
    parsed = []
    for item in lines:
        parsed.append(int(item.strip()))
    return parsed


def main():

    dk = Deck(3)
    cards_per_hand = 5

    for i in range(cards_per_hand):
        dk.deal()

    print("RULES")
    print("-- Enter a sequence of numbers corresponding to the cards which you'd like to exchange.")
    print("-- For ex.: \"1, 4, 5\"")
    print()

    while True:
        dk.display_current_hand()
        cards_to_exchange = input("> Enter numbers of cards to exchange: ")
        try:
            cards_to_exchange = parse_int_list(cards_to_exchange)
        except ValueError:
            print(">>> Invalid list input; please try again.")
            print(">>> For ex.: \"1, 3, 5\"")
            continue

        for i in cards_to_exchange:
            try:
                dk.exchange_card(i - 1)
            except ValueError:
                print(f">>> Card position out of range: {i}")
                print(">>> No exchange occurred for this entry.")



if __name__ == "__main__":
    main()


