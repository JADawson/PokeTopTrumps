import get_pokemon as gp


class Card:
    # a card has the details of the pokemon
    pass


class Deck(list):
    # a deck is a collection of cards

    def __init__(self, source: str, num_cards: int = 50, num_pokemon: int = 649):
        self.cards = []

        match source:
            case 'Pokedex':
                self.cards = gp.random_selection_csv(num_choices=num_cards)
            case 'API':
                self.cards = gp.random_selection_api(num_choices=num_cards, num_pokemon=num_pokemon)


class Hand(Deck):
    pass


class Round(Deck):
    pass

