import unittest
from random import choice, seed

from chapter_01 import FrenchCardDeck, Card, spades_high


class TestFrenchCardDeck(unittest.TestCase):

    def setUp(self):
        seed(123)
        self.deck = FrenchCardDeck()

    def test_french_card_deck_len(self):
        self.assertEqual(52, len(self.deck))

    def test_get_random_card(self):
        card = choice(self.deck)
        self.assertEqual(Card('2', 'hearts'), card)

    def test_sorting_by_spades_high(self):
        sorted_deck = sorted(self.deck, key=spades_high)
        self.assertEqual(Card('2', 'clubs'), sorted_deck[0])
        self.assertEqual(Card('A', 'spades'), sorted_deck[-1])


if __name__ == '__main__':
    unittest.main()
