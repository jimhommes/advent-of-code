import re


class Card:

    def __init__(self, cn, wn, on):
        self.card_number = int(cn)
        self.winning_numbers = wn
        self.own_numbers = on
        self.points = 0
        self.matches = 0

    def calculate_points(self):
        self.matches = len([own_number for own_number in self.own_numbers if own_number in self.winning_numbers])
        self.points = pow(2, self.matches - 1) if self.matches > 0 else 0

    def __repr__(self):
        return 'Card ' + str(self.card_number) + ': ' + str(self.points)


with open('input/4.txt') as f:
    lines = f.readlines()

cards = []
cards_with_copies = []
amount_of_cards = [1] * len(lines)
for card_index in range(len(lines)):
    line = lines[card_index]
    for card_repetition in range(amount_of_cards[card_index]):
        if card_repetition == 0:
            card = Card(re.findall(r'\d+', line.split(':')[0])[0],
                              [int(i) for i in line.split(': ')[1].split(' | ')[0].split(' ') if i != ''],
                              [int(i) for i in line.split(': ')[1].split(' | ')[1].split(' ') if i != ''])
            # Task 1
            card.calculate_points()

        # Task 2
        for card_index_repetition in range(card_index + 1, card_index + card.matches + 1):
            amount_of_cards[card_index_repetition] += 1

        cards_with_copies.append(card)
    cards.append(card)

print(cards)
print(sum([i.points for i in cards]))
print(len(cards_with_copies))